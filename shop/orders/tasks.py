from celery import shared_task
from django.core.mail import send_mail
from .models import Order

@shared_task
def order_created(order_id):
     """
     Задание по отправке уведомления по электронной почте
     при успешном создании заказа.
     """
     order = Order.objects.get(id=order_id)
     subject = f'Заказ номер {order.id}'
     message = f'Уважаемый/ая {order.first_name},\n\n' \
               f'Ваш заказ успешно оформлен!' \
               f'Номер вашего заказа: {order.id}.'
     mail_sent = send_mail(subject,
                           message,
                           'janetuyy@gmail.com',
                           [order.email])
     return mail_sent