from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView

from mailingApp.models import Client, Massage, Periodicity, Setting, Mailings


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
    success_url = reverse_lazy('#')


class MassageUpdateView(UpdateView):
    model = Massage
    fields = ('title', 'text',)
    success_url = reverse_lazy('#')


class MassageListView(ListView):
    model = Massage


class MassageDetailView(DetailView):
    model = Massage


class MassageDeleteView(DeleteView):
    model = Massage
    success_url = reverse_lazy('#')


class PeriodicityCreateView(CreateView):
    model = Periodicity
    fields = ('name', 'periodicity',)
    success_url = reverse_lazy('#')


class PeriodicityUpdateView(UpdateView):
    model = Periodicity
    fields = ('name', 'periodicity',)
    success_url = reverse_lazy('#')


class PeriodicityListView(ListView):
    model = Periodicity


class PeriodicityDetailView(DetailView):
    model = Periodicity


class PeriodicityDeleteView(DeleteView):
    model = Periodicity
    success_url = reverse_lazy('#')


class SettingCreateView(CreateView):
    model = Setting
    fields = ('name', 'at_start', 'at_end', 'periodicity',)
    success_url = reverse_lazy('#')


class SettingUpdateView(UpdateView):
    model = Setting
    fields = ('name', 'at_start', 'at_end', 'periodicity',)
    success_url = reverse_lazy('#')


class SettingListView(ListView):
    model = Setting


class SettingDetailView(DetailView):
    model = Setting


class SettingDeleteView(DeleteView):
    model = Setting
    success_url = reverse_lazy('#')


class MailingsCreateView(CreateView):
    model = Mailings
    fields = ('name', 'description', 'setting', 'massage', 'client',)
    success_url = reverse_lazy('#')


class MailingsUpdateView(UpdateView):
    model = Mailings
    fields = ('name', 'description', 'setting', 'massage', 'client',)
    success_url = reverse_lazy('#')


class MailingsListView(ListView):
    model = Mailings


class MailingsDetailView(DetailView):
    model = Mailings


class MailingsDeleteView(DeleteView):
    model = Mailings
    success_url = reverse_lazy('#')
