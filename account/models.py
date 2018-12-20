from django.db import models

from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.mail import send_mail
from .validators import UnicodeUsernameValidator


class MyUserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):

        if not email:
            raise ValueError('The given email must be set')
        if not username:
            raise ValueError('The given username must be set')
        email = self.normalize_email(email)
        username = self.model.normalize_username(username)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, username, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class MyUser(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(_('email address'), unique=True, blank=True,)

    username_validator = UnicodeUsernameValidator()

    username = models.CharField(_('username'), max_length=150, unique=True,
                                help_text=_('Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.'),
                                validators=[username_validator],
                                error_messages={'unique': _("A user with that username already exists."), }, )

    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=150, blank=True)

    is_staff = models.BooleanField(_('staff status'), default=False,
                                   help_text=_('Designates whether the user can log into this admin site.'), )
    is_active = models.BooleanField(_('active'), default=True,
                                    help_text=_('Designates whether this user should be treated as active. '
                                                'Unselect this instead of deleting accounts.'), )
    date_joined = models.DateTimeField(_('date joined'), default=timezone.now)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        verbose_name_plural = 'пользователи'
        verbose_name = 'пользователь'

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        """Send an email to this user."""
        send_mail(subject, message, from_email, [self.email], **kwargs)

    def __str__(self):
        return self.email








# from django.db import models
# from django.contrib.auth.models import BaseUserManager
# from django.contrib.auth.models import AbstractBaseUser
# from django.contrib.auth.models import PermissionsMixin
# from django.utils.translation import ugettext_lazy as _
#
#
# class MyUserManager(BaseUserManager):
#
#     def _create_user(self, email, password, **extra_fields):
#
#         if not email:
#             raise ValueError('The Email must be set')
#         email = self.normalize_email(email)
#         user = self.model(email=email, **extra_fields)
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#     def create_superuser(self, email, password, **extra_fields):
#         extra_fields.setdefault('is_staff', True)
#         extra_fields.setdefault('is_superuser', True)
#         extra_fields.setdefault('is_active', True)
#
#         if extra_fields.get('is_staff') is not True:
#             raise ValueError('Superuser must have is_staff=True.')
#         if extra_fields.get('is_superuser') is not True:
#             raise ValueError('Superuser must have is_superuser=True.')
#         return self._create_user(email, password, **extra_fields)
#
#
# class User(AbstractBaseUser, PermissionsMixin):
#     email = models.EmailField(unique=True, null=True, verbose_name='адрес электронной почты')
#     username = models.CharField(max_length=100, unique=True, null=True, verbose_name='пользователь')
#     is_staff = models.BooleanField(_('staff status'), default=False,)
#     is_active = models.BooleanField(_('active'), default=True, )
#
#     USERNAME_FIELD = 'email'
#     objects = MyUserManager()
#
#     class Meta:
#         verbose_name_plural = 'пользователи'
#         verbose_name = 'пользоветель'
#
#     def __str__(self):
#         return self.email
#
#     # def get_full_name(self):
#     #     return self.email
#     #
#     # def get_short_name(self):
#     #     return self.email
#
#
# class UserExtended(models.Model):
#
#     # CHOICE_MONTH = (
#     #     ('январь', 'январь'),
#     #     ('февраль', 'февраль'),
#     #     ('март', 'март'),
#     #     ('апрель', 'апрель'),
#     #     ('май', 'май'),
#     #     ('июнь', 'июнь'),
#     #     ('июль', 'июль'),
#     #     ('август', 'август'),
#     #     ('сентябрь', 'сентябрь'),
#     #     ('октябрь', 'октябрь'),
#     #     ('ноябрь', 'ноябрь'),
#     #     ('декабрь', 'декабрь'),
#     # )
#     # birthday = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(31)],
#     #                                verbose_name='день рождения')
#     # month_of_birth = models.CharField(max_length=20, choices=CHOICE_MONTH, verbose_name='месяц рождения')
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='UserExtended',
#                                 verbose_name='электронная почта')
#     avatar = models.ImageField(upload_to='images', blank=True, height_field=120, width_field=120,
#                                verbose_name='аватара', help_text='максимальный размер аватара 120х120')
#     country_list = models.CharField(max_length=100, verbose_name='страна пользователя')
#     first_name = models.CharField(max_length=100, verbose_name='имя пользователя')
#     last_name = models.CharField(max_length=100, verbose_name='фамилия пользователя')
#     birthday = models.IntegerField(verbose_name='день рождения')
#     month_of_birth = models.CharField(max_length=20, verbose_name='месяц рождения')
#     year_of_birth = models.IntegerField(verbose_name='год рождения')
#     news_and_info = models.BooleanField(verbose_name='новости и информация')
#     privacy_policy = models.BooleanField(verbose_name='политика конфиденциальности')
#
#     def __str__(self):
#         return f'{self.user.email}'
#
#     class Meta:
#         verbose_name_plural = 'дополнительные поля пользователей'
#         verbose_name = "дополнительное поле пользователя"
#
