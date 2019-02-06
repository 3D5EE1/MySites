from django.db import models

# Create your models here.


class Message(models.Model):
    application = models.CharField(max_length=100, verbose_name='имя приложения')
    name = models.CharField(max_length=50, verbose_name='имя')
    email = models.EmailField(verbose_name='емейл')
    subject = models.CharField(max_length=100, verbose_name='тема')
    data_time = models.DateTimeField(auto_now_add=True, verbose_name='дата и время')
    message = models.TextField(verbose_name='сообщение')

    def __str__(self):
        return f'{self.name} {self.email}'

    class Meta:
        verbose_name_plural = 'Сообщения'
        verbose_name = 'Сообщение'




