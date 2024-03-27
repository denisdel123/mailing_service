from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailingApp.models import Client, Massage, Attempt, Mailing


class ClientCreateView(CreateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'description',)
    success_url = reverse_lazy('mailingApp:client_list')


class ClientUpdateView(UpdateView):
    model = Client
    fields = ('first_name', 'last_name', 'email', 'description',)

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:client_detail', kwargs={'pk': object_id})
        return detail_url


class ClientListView(ListView):
    model = Client


def main(request):
    return render(request, 'mailingApp/main.html')


class ClientDetailView(DetailView):
    model = Client

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:client_detail', kwargs={'pk': object_id})
        return detail_url


class ClientDeleteView(DeleteView):
    model = Client
    success_url = reverse_lazy('mailingApp:client_list')


class MassageCreateView(CreateView):
    model = Massage
    fields = ('title', 'text',)
    success_url = reverse_lazy('mailingApp:massage_list')


class MassageUpdateView(UpdateView):
    model = Massage
    fields = ('title', 'text',)

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:massage_detail', kwargs={'pk': object_id})
        return detail_url


class MassageListView(ListView):
    model = Massage


class MassageDetailView(DetailView):
    model = Massage

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:massage_detail', kwargs={'pk': object_id})
        return detail_url


class MassageDeleteView(DeleteView):
    model = Massage
    success_url = reverse_lazy('mailingApp:massage_list')


class MailingCreateView(CreateView):
    model = Mailing
    fields = ('name', 'description', 'periodicity', 'at_start', 'at_end', 'massage', 'client', 'next_run',)
    success_url = reverse_lazy('mailingApp:mailing_list')


class MailingUpdateView(UpdateView):
    model = Mailing
    fields = ('name', 'description', 'periodicity', 'at_start', 'at_end', 'massage', 'client', 'next_run',)

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:mailing_detail', kwargs={'pk': object_id})
        return detail_url


class MailingListView(ListView):
    model = Mailing


class MailingDetailView(DetailView):
    model = Mailing

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:mailing_detail', kwargs={'pk': object_id})
        return detail_url


class MailingDeleteView(DeleteView):
    model = Mailing
    success_url = reverse_lazy('mailingApp:mailing_list')


class AttemptListView(ListView):
    model = Attempt

    def get_queryset(self):
        mailing_id = self.kwargs.get('mailing_id')
        queryset = super().get_queryset().filter(mailing__pk=mailing_id)
        return queryset

    def get_success_url(self):
        mailing_id = self.kwargs.get('mailing_id')
        detail_url = reverse_lazy('mailingApp:attempt_detail', kwargs={'pk': mailing_id})
        return detail_url


class AttemptDetailView(DetailView):
    model = Attempt

    def get_success_url(self):
        object_id = self.object.pk
        detail_url = reverse_lazy('mailingApp:attempt_detail', kwargs={'pk': object_id})
        return detail_url
