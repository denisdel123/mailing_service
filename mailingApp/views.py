from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailingApp.models import Massage, Attempt, Mailing

@login_required
def main(request):
    return render(request, 'mailingApp/main.html')


class MassageCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Massage
    fields = ('title', 'text',)
    permission_required = 'mailingApp.add_massage'
    success_url = reverse_lazy('mailingApp:massage_list')


class MassageUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Massage
    fields = ('title', 'text',)
    permission_required = 'mailingApp.change_massage'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:massage_detail', kwargs={'pk': object_id})
        return detail_url


class MassageListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Massage
    permission_required = 'mailingApp.view_massage'


class MassageDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Massage
    permission_required = 'mailingApp.view_massage'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:massage_detail', kwargs={'pk': object_id})
        return detail_url


class MassageDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Massage
    permission_required = 'mailingApp.delete_massage'
    success_url = reverse_lazy('mailingApp:massage_list')


class MailingCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Mailing
    permission_required = 'mailingApp.add_mailing'
    fields = ('name', 'description', 'periodicity', 'at_start', 'at_end', 'massage', 'user', 'next_run',)
    success_url = reverse_lazy('mailingApp:mailing_list')


class MailingUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Mailing
    permission_required = 'mailingApp.change_mailing'
    fields = ('name', 'description', 'periodicity', 'at_start', 'at_end', 'massage', 'user', 'next_run',)

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:mailing_detail', kwargs={'pk': object_id})
        return detail_url


class MailingListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = Mailing
    permission_required = 'mailingApp.view_mailing'


class MailingDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Mailing
    permission_required = 'mailingApp.view_mailing'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:mailing_detail', kwargs={'pk': object_id})
        return detail_url


class MailingDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Mailing
    permission_required = 'mailingApp.delete_mailing'
    success_url = reverse_lazy('mailingApp:mailing_list')


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


class AttemptDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Attempt
    permission_required = 'mailingApp.view_attempt'

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:attempt_detail', kwargs={'pk': object_id})
        return detail_url

