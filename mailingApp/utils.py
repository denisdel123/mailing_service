from datetime import timedelta
from dateutil.relativedelta import relativedelta
import os
import logging
from django.core.mail import send_mail
from django.utils import timezone

from mailingApp.models import Mailing, Attempt

ADDRESS_MAIL_RU = os.environ.get("ADDRESS_MAIL_RU")


def mailing_filter():
    date_time = timezone.now()
    mailings = Mailing.objects.all()

    for mailing in mailings:
        at_end = mailing.at_end
        if at_end <= date_time:
            mailing.status = 'completed'
            mailing.save()
        else:
            pass
    mailings_filtered = mailings.filter(status='create')

    send_email(mailings_filtered)


def send_email(mailing):
    logging.info("send_email")
    date_time = timezone.now()
    for objects in mailing:

        at_start = objects.at_start
        at_end = objects.at_end
        next_run = objects.next_run

        if at_start <= date_time <= at_end and date_time >= next_run:
            objects.status = 'launched'
            title = objects.massage.title
            text = objects.massage.text
            users = objects.user.all()
            users_email = [user.email for user in users]

            try:
                status = send_mail(subject=title,
                                   message=text,
                                   from_email=ADDRESS_MAIL_RU,
                                   recipient_list=users_email,
                                   )
                Attempt.objects.create(status_attempt=status, mailing=objects)

            except Exception as e:
                Attempt.objects.create(status_attempt=False, mailing=objects, answer_mail=e)

            if objects.periodicity == 'daily':
                objects.next_run = date_time + timedelta(days=1)
                objects.status = 'create'
            elif objects.periodicity == 'weekly':
                objects.next_run = date_time + timedelta(weeks=1)
                objects.status = 'create'
            elif objects.periodicity == 'monthly':
                objects.next_run = date_time + relativedelta(months=1)
                objects.status = 'create'
            elif objects.periodicity == 'yearly':
                objects.next_run = date_time + relativedelta(years=1)
                objects.status = 'create'
            else:
                objects.status = 'completed'
            objects.save()
