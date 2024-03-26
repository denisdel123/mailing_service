import smtplib
import os

PASSWORD_MAIL_RU = os.getenv('PASSWORD_MAIL_RU')
ADDRESS_MAIL_RU = os.environ.get("ADDRESS_MAIL_RU")
GETTER_MAIL = 'denis_belenko@mail.ru'


def send_massage(objects):
    with smtplib.SMTP('smtp.mail.ru', 587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        smtp.login(ADDRESS_MAIL_RU, PASSWORD_MAIL_RU)

        subject = 'hello Denis'
        body = 'it is test for your curse work'

        msg = f'subject: {objects.title}\n\n{objects.text}'

        smtp.sendmail(ADDRESS_MAIL_RU, GETTER_MAIL, msg)


if __name__ == '__main__':
    ...
