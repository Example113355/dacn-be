from django.conf import settings
from django.core.mail import send_mail

from django_core.exceptions import EmailServiceError


class EmailService:
    @staticmethod
    def send_email(subject: str, message: str, recipient: str):
        try:
            send_mail(subject, message, settings.EMAIL_HOST_USER, [recipient])
        except Exception as e:
            raise EmailServiceError(str(e))
