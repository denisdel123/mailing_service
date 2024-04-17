from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailingApp.forms import \
    SuperuserMassageForm, UserMassageForm, SuperuserClientForm, \
    UserClientForm, SuperuserMailingForm, UserMailingForm, ManagerMailingForm
from mailingApp.models import Massage, Attempt, Mailing, Client

"""Главная страница"""


@login_required
def main(request):
    return render(request, 'mailingApp/main.html')


"""Создание клиентов"""


class ClientCreateView(LoginRequiredMixin, CreateView):
    model = Client

    def get_form_class(self):
        if self.request.user.is_superuser:
            form_class = SuperuserClientForm
            return form_class
        else:
            form_class = UserClientForm
            return form_class

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:client_detail', kwargs={'pk': object_id})
        return detail_url


"""Список клиентов"""


class ClientListView(LoginRequiredMixin, ListView):
    model = Client

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.has_perm('mailingApp.set_view'):
            queryset = super().get_queryset().all()
            return queryset
        else:
            user_id = self.request.user.pk
            queryset = super().get_queryset().filter(owner__id=user_id)
            return queryset


"""Страница клиента"""


class ClientDetailView(LoginRequiredMixin, DetailView):
    model = Client

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:client_detail', kwargs={'pk': object_id})
        return detail_url


"""Редактирование клиента"""


class ClientUpdateView(LoginRequiredMixin, UpdateView):
    model = Client

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:client_detail', kwargs={'pk': object_id})
        return detail_url

    def get_form_class(self):
        if self.request.user.is_superuser:
            form_class = SuperuserClientForm
            return form_class

        else:
            form_class = UserClientForm
            return form_class


"""Удаление клиента"""


class ClientDeleteView(LoginRequiredMixin, DeleteView):
    model = Client
    success_url = 'mailingApp:client_list'


"""Создание сообщения"""


class MassageCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Massage
    fields = ('title', 'text',)
    permission_required = 'mailingApp.add_massage'
    success_url = reverse_lazy('mailingApp:massage_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_class(self):
        if self.request.user.is_superuser:
            form_class = SuperuserMassageForm
            return form_class
        else:
            form_class = UserMassageForm
            return form_class


""" Редактирование сообщения"""


class MassageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Massage
    fields = ('title', 'text',)
    permission_required = 'mailingApp.change_massage'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:massage_detail', kwargs={'pk': object_id})
        return detail_url

    def get_form_class(self):
        if self.request.user.is_superuser:
            form_class = SuperuserMassageForm
            return form_class
        else:
            form_class = UserMassageForm
            return form_class


"""Список сообщения"""


class MassageListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Massage
    permission_required = 'mailingApp.view_massage'

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.has_perm('mailingApp.set_view'):
            queryset = super().get_queryset().all()
            return queryset
        else:
            user_id = self.request.user.pk
            queryset = super().get_queryset().filter(owner__id=user_id)
            return queryset


"""Страница сообщения"""


class MassageDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Massage
    permission_required = 'mailingApp.view_massage'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:massage_detail', kwargs={'pk': object_id})
        return detail_url


"""Удаление сообщения"""


class MassageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Massage
    permission_required = 'mailingApp.delete_massage'
    success_url = reverse_lazy('mailingApp:massage_list')


"""Создание рассылки"""


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    permission_required = 'mailingApp.add_mailing'
    success_url = reverse_lazy('mailingApp:mailing_list')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.owner = self.request.user
        self.object.save()
        return super().form_valid(form)

    def get_form_class(self):
        if self.request.user.is_superuser:
            form_class = SuperuserMailingForm
            return form_class
        else:
            form_class = UserMailingForm
            return form_class


"""Редактирование рассылки"""


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    permission_required = 'mailingApp.change_mailing'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:mailing_detail', kwargs={'pk': object_id})
        return detail_url

    def get_form_class(self):
        if self.request.user.is_superuser:
            form_class = SuperuserMailingForm
            return form_class
        elif self.request.user.has_perm('mailingApp.set_status'):
            form_class = ManagerMailingForm
            return form_class
        else:
            form_class = UserMailingForm
            return form_class


"""Список рассылок"""


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailing
    permission_required = 'mailingApp.view_mailing'

    def get_queryset(self):
        if self.request.user.is_superuser or self.request.user.has_perm('mailingApp.set_view'):
            queryset = super().get_queryset().all()
            return queryset
        else:
            user_id = self.request.user.pk
            queryset = super().get_queryset().filter(owner__id=user_id)
            return queryset


"""Страница рассылки"""


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Mailing
    permission_required = 'mailingApp.view_mailing'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:mailing_detail', kwargs={'pk': object_id})
        return detail_url


"""Удаление рассылки"""


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    permission_required = 'mailingApp.delete_mailing'
    success_url = reverse_lazy('mailingApp:mailing_list')


"""Список попыток рассылки"""


class AttemptListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Attempt
    permission_required = 'mailingApp.view_attempt'

    def get_queryset(self):
        mailing_id = self.kwargs.get('mailing_id')
        queryset = super().get_queryset().filter(mailing__pk=mailing_id)
        return queryset

    def get_success_url(self):
        mailing_id = self.kwargs.get('mailing_id')
        detail_url = reverse_lazy('mailingApp:attempt_detail', kwargs={'pk': mailing_id})
        return detail_url


"""Страница попытки рассылки"""


class AttemptDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Attempt
    permission_required = 'mailingApp.view_attempt'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:attempt_detail', kwargs={'pk': object_id})
        return detail_url
