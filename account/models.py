from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class UserExtended(models.Model):

    CHOICE_MONTH = (
        ('январь', 'январь'),
        ('февраль', 'февраль'),
        ('март', 'март'),
        ('апрель', 'апрель'),
        ('май', 'май'),
        ('июнь', 'июнь'),
        ('июль', 'июль'),
        ('август', 'август'),
        ('сентябрь', 'сентябрь'),
        ('октябрь', 'октябрь'),
        ('ноябрь', 'ноябрь'),
        ('декабрь', 'декабрь'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserExtended',
                                verbose_name='пользователь')
    avatar = models.ImageField(upload_to='images', blank=True, height_field=120, width_field=120,
                               verbose_name='аватара', help_text='максимальный размер аватара 120х120')
    country_list = models.CharField(max_length=100, verbose_name='страна пользователя')
    birthday = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)],
                                   verbose_name='день рождения')
    month_of_birth = models.CharField(max_length=20, choices=CHOICE_MONTH, verbose_name='месяц рождения')
    year_of_birth = models.IntegerField(verbose_name='год рождения')
    privacy_policy = models.BooleanField(verbose_name='политика конфиденциальности')

    def __str__(self):
        return f'{self.user.username}    {self.user.email}'

    class Meta:
        verbose_name_plural = 'дополнительные поля пользователей'
        verbose_name = "дополнительное поле пользователя"
