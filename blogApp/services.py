from random import sample

from blogApp.models import Blog
from mailingApp.models import Mailing, Client


def list_main():
    mailing_count = Mailing.objects.all().count
    mailing_active_count = Mailing.objects.all().filter(status='create').count()
    client_count = Client.objects.all().count
    queryset_all = Blog.objects.all().filter(is_published=True)
    if queryset_all:
        queryset = sample(list(queryset_all), 3)
    else:
        queryset = None

    context = {
        'mailing_count': mailing_count,
        'mailing_active_count': mailing_active_count,
        'client_count': client_count,
        'queryset': queryset,
    }
    return context



