from django.core.mail import send_mail
import os

from config.settings import ADDRESS_MAIL_RU
from usersApp.models import User


def send_mail_all(subject, message, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        recipient_list=recipient_list,
    )
