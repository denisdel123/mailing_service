from django.urls import path
from django.views.decorators.cache import cache_page

from mailingApp.apps import MailingappConfig
from mailingApp.views import main, \
    MailingListView, MailingCreateView, MailingUpdateView, \
    MailingDetailView, MailingDeleteView, MassageListView, MassageCreateView, MassageDetailView, MassageUpdateView, \
    MassageDeleteView, AttemptListView, AttemptDetailView, ClientListView, ClientCreateView, ClientDetailView, \
    ClientUpdateView, ClientDeleteView

app_name = MailingappConfig.name

urlpatterns = [

    path('', main, name='main'),

    path('client/list', cache_page(60)(ClientListView.as_view()), name='client_list'),
    path('client/create', ClientCreateView.as_view(), name='client_create'),
    path('client/<int:pk>', cache_page(60)(ClientDetailView.as_view()), name='client_detail'),
    path('client/update/<int:pk>', ClientUpdateView.as_view(), name='client_update'),
    path('client/delete/<int:pk>', ClientDeleteView.as_view(), name='client_delete'),

    path('massage/list/', MassageListView.as_view(), name='massage_list'),
    path('massage/create/', MassageCreateView.as_view(), name='massage_create'),
    path('massage/<int:pk>', MassageDetailView.as_view(), name='massage_detail'),
    path('massage/update/<int:pk>', MassageUpdateView.as_view(), name='massage_update'),
    path('massage/delete/<int:pk>', MassageDeleteView.as_view(), name='massage_delete'),

    path('mailing/<int:mailing_id>/attempt/list/', AttemptListView.as_view(), name='attempt_list'),
    path('attempt/detail/<int:pk>', AttemptDetailView.as_view(), name='attempt_detail'),

    path('mailing/list', MailingListView.as_view(), name='mailing_list'),
    path('mailing/create', MailingCreateView.as_view(), name='mailing_create'),
    path('mailing/detail/<int:pk>', MailingDetailView.as_view(), name='mailing_detail'),
    path('mailing/update/<int:pk>', MailingUpdateView.as_view(), name='mailing_update'),
    path('mailing/delete<int:pk>', MailingDeleteView.as_view(), name='mailing_delete'),



]
