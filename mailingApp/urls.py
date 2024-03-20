from django.urls import path

from mailingApp.apps import MailingappConfig
from mailingApp.views import ClientListView, main, ClientCreateView, ClientUpdateView, ClientDetailView, \
    ClientDeleteView, SettingListView, PeriodicityCreateView, PeriodicityListView, PeriodicityUpdateView, \
    PeriodicityDetailView, PeriodicityDeleteView, MailingsListView, MailingsCreateView, MailingsUpdateView, \
    MailingsDetailView, MailingsDeleteView

app_name = MailingappConfig.name





urlpatterns = [

    path('', main, name='main'),

    path('client/list', ClientListView.as_view(), name='client_list'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>', ClientDetailView.as_view(), name='client_detail'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('mailing/list', MailingsListView.as_view(), name='mailing_list'),
    path('mailing/create', MailingsCreateView.as_view(), name='mailing_create'),
    path('mailing/update/<int:pk>', MailingsUpdateView.as_view(), name='mailing_update'),
    path('mailing/detail/<int:pk>', MailingsDetailView.as_view(), name='mailing_detail'),
    path('mailing/delete<int:pk>', MailingsDeleteView.as_view(), name='mailing_delete'),

    path('periodicity/list', PeriodicityListView.as_view(), name='periodicity_list'),
    path('periodicity/create', PeriodicityCreateView.as_view(), name='periodicity_create'),
    path('periodicity/update/<int:pk>', PeriodicityUpdateView.as_view(), name='periodicity_update'),
    path('periodicity/detail/<int:pk>', PeriodicityDetailView.as_view(), name='periodicity_detail'),
    path('periodicity/delete<int:pk>', PeriodicityDeleteView.as_view(), name='periodicity_delete'),

]
