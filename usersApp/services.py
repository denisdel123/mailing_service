from django.contrib.auth import get_user_model
from django.core.exceptions import ObjectDoesNotExist
from django.core.mail import send_mail
import os

from django.utils.crypto import get_random_string

from config.settings import ADDRESS_MAIL_RU

User = get_user_model()


def send_mail_all(subject, message, recipient_list):
    try:
        send_mail(
            subject=subject,
            message=message,
            recipient_list=recipient_list,
            from_email=ADDRESS_MAIL_RU
        )
        return True
    except Exception as error:
        return error


def send_new_password(email):
    if not email:
        return {'success': 'usersApp/forgot_password.html', 'context': {'error_message': 'Введите Email.'}}

    try:
        user = User.objects.get(email=email)
    except User.DoesNotExist:
        return {'success': 'usersApp/forgot_password.html', 'context': {'error_message': 'Пользователя с таким Email '
                                                                                         'не существует.'}}

    new_password = get_random_string(10)
    subject = f'Смена пароля'
    message = f'Ваш новый пароль: {new_password}'

    send_result = send_mail_all(subject, message, [email])
    if send_result is True:
        user.set_password(new_password)
        user.save()
        return {'success': 'usersApp:login'}
    else:
        message_error = f'Ошибка отправки Email: {send_result}'
        return {'success': 'usersApp/forgot_password.html', 'context': {'error_message': message_error}}
