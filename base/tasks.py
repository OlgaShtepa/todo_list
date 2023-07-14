from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth.models import User


@shared_task
def send_welcome_email(user_id):
    user = User.objects.get(id=user_id)
    subject = 'Welcome to our Todo list!'
    message = f'Dear {user.username}, thank for using our app!'
    from_email = 'estingcelery.0@gmail.com'
    to_email = [user.email]
    send_mail(subject, message, from_email, to_email)
