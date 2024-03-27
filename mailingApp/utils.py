import datetime
from dateutil.relativedelta import relativedelta
import os
from django.utils import timezone
from django.core.mail import send_mail
from mailingApp.models import Mailing, Attempt

PASSWORD_MAIL_RU = os.getenv('PASSWORD_MAIL_RU')
ADDRESS_MAIL_RU = os.environ.get("ADDRESS_MAIL_RU")
GETTER_MAIL = 'denis_belenko@mail.ru'


def mailing_filter():
    date_time = timezone.now()

    mailings = Mailing.objects.all()
    for mailing in mailings:
        if mailing.at_end >= date_time:
            mailing.status = 'completed'
            mailing.save()
        else:
            pass
    mailings_filtered = mailings.filter(status='create')

    send_email(mailings_filtered)


def send_email(mailing):
    date_time = timezone.now()
    for objects in mailing:
        if objects.at_start <= date_time <= objects.at_end and date_time >= objects.next_run:
            objects.status = 'launched'
            title = objects.massage.title
            text = objects.massage.text
            clients = objects.client.all()
            clients_email = [client.email for client in clients]

            try:
                status = send_mail(subject=title,
                                   message=text,
                                   from_email=ADDRESS_MAIL_RU,
                                   recipient_list=clients_email,
                                   )
                Attempt.objects.create(status_attempt=status, mailing=objects)

            except Exception as e:
                Attempt.objects.create(status_attempt=False, mailing=objects, answer_mail=e)

    if mailing.periodicity == 'daily':
        mailing.next_run = date_time + datetime.timedelta(days=1)
        mailing.status = 'create'
    elif mailing.periodicity == 'weekly':

        mailing.next_run = date_time + datetime.timedelta(weeks=1)
        mailing.status = 'create'
    elif mailing.periodicity == 'monthly':
        mailing.next_run = date_time + relativedelta(months=1)
        mailing.status = 'create'
    elif mailing.periodicity == 'yearly':
        mailing.next_run = date_time + relativedelta(years=1)
        mailing.status = 'create'
    else:
        mailing.status = 'completed'

    mailing.save()

