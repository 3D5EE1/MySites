# Generated by Django 2.1.3 on 2018-12-17 03:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('email', models.EmailField(max_length=254, null=True, unique=True, verbose_name='адрес электронной почты')),
                ('username', models.CharField(max_length=100, null=True, unique=True, verbose_name='пользователь')),
                ('is_staff', models.BooleanField(default=False, verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'пользоветель',
                'verbose_name_plural': 'пользователи',
            },
        ),
        migrations.CreateModel(
            name='UserExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, height_field=120, help_text='максимальный размер аватара 120х120', upload_to='images', verbose_name='аватара', width_field=120)),
                ('country_list', models.CharField(max_length=100, verbose_name='страна пользователя')),
                ('first_name', models.CharField(max_length=100, verbose_name='имя пользователя')),
                ('last_name', models.CharField(max_length=100, verbose_name='фамилия пользователя')),
                ('birthday', models.IntegerField(verbose_name='день рождения')),
                ('month_of_birth', models.CharField(max_length=20, verbose_name='месяц рождения')),
                ('year_of_birth', models.IntegerField(verbose_name='год рождения')),
                ('news_and_info', models.BooleanField(verbose_name='новости и информация')),
                ('privacy_policy', models.BooleanField(verbose_name='политика конфиденциальности')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserExtended', to=settings.AUTH_USER_MODEL, verbose_name='электронная почта')),
            ],
            options={
                'verbose_name': 'дополнительное поле пользователя',
                'verbose_name_plural': 'дополнительные поля пользователей',
            },
        ),
    ]