from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView, PasswordChangeView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from usersApp.forms import UserForm, UserUpdateForm, SuperuserUpdateForm, ManagerUpdateForm
from usersApp.models import User
from usersApp.services import send_mail_all, send_new_password, s_email_confirm


class LoginView(BaseLoginView):
    template_name = 'usersApp/login.html'


class LogoutView(BaseLogoutView):
    ...


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
        elif self.request.user.has_perm('usersApp.set_active'):
            form_class = ManagerUpdateForm
            return form_class
        else:
            form_class = UserUpdateForm
            return form_class


class UserListView(PermissionRequiredMixin, LoginRequiredMixin, ListView):
    model = User
    permission_required = 'userApp.view_user'


class UserDetailView(LoginRequiredMixin, DetailView):
    model = User

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('usersApp:detail', kwargs={'pk': object_id})

        return detail_url


class UserDeleteView(LoginRequiredMixin, DeleteView):
    model = User
    success_url = reverse_lazy('usersApp:list')


def forgot_password(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        answer = send_new_password(email)

        if len(answer) == 1:
            return redirect(answer['success'])
        elif len(answer) == 2:
            messages.error(request, answer['context']['error_message'])
            return render(request, answer['success'], answer['context'])


class PasswordChange(LoginRequiredMixin, PasswordChangeView):
    template_name = 'usersApp/change_password.html'
    success_url = reverse_lazy('usersApp:list')


@login_required()
def send_code(request):
    if request.method == 'POST':
        user = request.user
        email = user.email
        s_email_confirm(email)

        return render(request, 'usersApp/email_confirm.html')


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
