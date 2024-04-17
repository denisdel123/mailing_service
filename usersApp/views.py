from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView, PasswordChangeView
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from usersApp.forms import UserForm, UserUpdateForm, SuperuserUpdateForm
from usersApp.models import User
from usersApp.services import send_mail_all, send_new_password, s_email_confirm

"""Вход по почте и паролю"""


class LoginView(BaseLoginView):
    template_name = 'usersApp/login.html'


"""Выход из профиля"""


class LogoutView(BaseLogoutView):
    ...


"""Регистрация пользователя"""


class RegistrationView(CreateView):
    model = User
    form_class = UserForm
    success_url = reverse_lazy('usersApp:login')
    template_name = 'usersApp/registration.html'

    def form_valid(self, form):
        new_user = form.save(commit=False)
        subject = f'Регистрация'
        message = 'Поздравляю вы зарегистрировались на нашем сайте!'
        user_email = [new_user.email]

        if send_mail_all(subject, message, user_email) is True:
            new_user.is_active = True
            new_user.save()
            return super().form_valid(form)
        else:
            error_message = 'Произошла ошибка при отправки Email, попробуйте снова!'
            messages.error(self.request, error_message)
            return self.form_invalid(form)


"""Редактирование пользователя"""


class UserUpdateView(LoginRequiredMixin, UpdateView):
    model = User

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('usersApp:detail', kwargs={'pk': object_id})
        return detail_url

    def get_form_class(self):
        if self.request.user.is_superuser:
            form_class = SuperuserUpdateForm
            return form_class
        else:
            form_class = UserUpdateForm
            return form_class


"""Список всех пользователей"""


class UserListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = User
    permission_required = 'usersApp.view_user'

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_superuser:
            queryset = queryset.exclude(is_superuser=True)
        elif self.request.user.has_perm('usersApp.view_user'):
            email = self.request.user.email
            queryset = queryset.exclude(email=email).exclude(is_superuser=True)
        return queryset


"""Контроллер для менеджеров """


class UserDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = User
    permission_required = 'usersApp.view_user'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('usersApp:detail', kwargs={'pk': object_id})
        return detail_url

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context


"""Посещение своего профиля"""


class UserProfile(LoginRequiredMixin, DetailView):
    model = User

    def get_object(self, queryset=None):
        return self.request.user


"""Удаление пользователя"""


class UserDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('usersApp:list')
    permission_required = 'usersApp.delete_view'


"""Востановление пароля по Email"""


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        answer = send_new_password(email)

        if len(answer) == 1:
            return redirect(answer['success'])
        elif len(answer) == 2:
            messages.error(request, answer['context']['error_message'])
            return render(request, answer['success'], answer['context'])


"""Изменение Пароля через профиль"""


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usersApp/change_password.html'
    success_url = reverse_lazy('usersApp:list')


"""Подтверждение почты"""


@login_required()
def send_code(request):
    if request.method == 'POST':
        user = request.user
        email = user.email
        s_email_confirm(email)

        return render(request, 'usersApp/email_confirm.html')


"""Получение кода через форму и его проверка"""


@login_required()
def email_confirm(request):
    if request.method == 'POST':
        user = request.user
        code = request.POST.get('text')
        if user.code == code:
            user.is_confirm = True
            user.save()
            return redirect(reverse('usersApp:detail', kwargs={'pk': user.pk}))

        else:
            messages.error(request, 'не верный код попробуйте снова!')

        return render(request, 'usersApp/email_confirm.html')


"""Возможность Блокировать и разблокировать пользователей"""


@login_required()
@permission_required('usersApp.set_active')
def block_user(request, pk):
    if request.method == 'POST':
        obj = get_object_or_404(User, pk=pk)
        obj.is_active = not obj.is_active
        obj.save()
        return redirect('usersApp:detail', pk=pk)


class BlockUser(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = User
    permission_required = 'usersApp.set_active'
    fields = ['is_active']
    template_name = 'usersApp/user_form.html'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.is_active = not self.object.is_active
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('usersApp:detail', kwargs={'pk': object_id})
        return detail_url
