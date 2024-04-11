from django.contrib.auth.views import LoginView as BaseLoginView, LogoutView as BaseLogoutView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView, DeleteView

from usersApp.forms import UserForm, UserUpdateForm
from usersApp.models import User
from usersApp.services import send_mail_all


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
        new_user = form.save()
        subject = f'Регистрация'
        message = 'Поздравляю вы зарегистрировались на нашем сайте!'
        user_email = [new_user.email]
        try:
            send_mail_all(subject, message, user_email)
            new_user.is_active = True
        except Exception as e:
            pass

        return super().form_valid(form)


class UserUpdateView(UpdateView):
    model = User
    form_class = UserUpdateForm
    success_url = reverse_lazy('usersApp:update')

    def get_object(self, queryset=None):
        return self.request.user


class UserListView(ListView):
    model = User


class UserDetailView(DetailView):
    model = User

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('usersApp:detail', kwargs={'pk': object_id})
        return detail_url


class UserDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('usersApp:list')
