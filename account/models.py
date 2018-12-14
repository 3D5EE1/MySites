from django.db import models
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _


class MyUserManager(BaseUserManager):

    def _create_user(self, email, password, **extra_fields):

        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
        return self._create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True, null=True, verbose_name='адрес электронной почты')
    username = models.CharField(max_length=100, unique=True, null=True, verbose_name='пользователь')
    is_staff = models.BooleanField(_('staff status'), default=False,)
    is_active = models.BooleanField(_('active'), default=True, )

    USERNAME_FIELD = 'email'
    objects = MyUserManager()

    class Meta:
        verbose_name_plural = 'пользователи'
        verbose_name = 'пользоветель'

    def __str__(self):
        return self.email

    # def get_full_name(self):
    #     return self.email
    #
    # def get_short_name(self):
    #     return self.email


class UserExtended(models.Model):

    # CHOICE_MONTH = (
    #     ('январь', 'январь'),
    #     ('февраль', 'февраль'),
    #     ('март', 'март'),
    #     ('апрель', 'апрель'),
    #     ('май', 'май'),
    #     ('июнь', 'июнь'),
    #     ('июль', 'июль'),
    #     ('август', 'август'),
    #     ('сентябрь', 'сентябрь'),
    #     ('октябрь', 'октябрь'),
    #     ('ноябрь', 'ноябрь'),
    #     ('декабрь', 'декабрь'),
    # )
    # birthday = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)],
    #                                verbose_name='день рождения')
    # month_of_birth = models.CharField(max_length=20, choices=CHOICE_MONTH, verbose_name='месяц рождения')

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserExtended',
                                verbose_name='электронная почта')
    avatar = models.ImageField(upload_to='images', blank=True, height_field=120, width_field=120,
                               verbose_name='аватара', help_text='максимальный размер аватара 120х120')
    country_list = models.CharField(max_length=100, verbose_name='страна пользователя')
    first_name = models.CharField(max_length=100, verbose_name='имя пользователя')
    last_name = models.CharField(max_length=100, verbose_name='фамилия пользователя')
    birthday = models.IntegerField(verbose_name='день рождения')
    month_of_birth = models.CharField(max_length=20, verbose_name='месяц рождения')
    year_of_birth = models.IntegerField(verbose_name='год рождения')
    news_and_info = models.BooleanField(verbose_name='новости и информация')
    privacy_policy = models.BooleanField(verbose_name='политика конфиденциальности')

    def __str__(self):
        return f'{self.user.email}'

    class Meta:
        verbose_name_plural = 'дополнительные поля пользователей'
        verbose_name = "дополнительное поле пользователя"

