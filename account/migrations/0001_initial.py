# Generated by Django 2.1.4 on 2018-12-11 10:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserExtended',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avatar', models.ImageField(blank=True, height_field=120, help_text='максимальный размер аватара 120х120', upload_to='images', verbose_name='аватара', width_field=120)),
                ('country_list', models.CharField(max_length=100, verbose_name='страна пользователя')),
                ('birthday', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(31)], verbose_name='день рождения')),
                ('month_of_birth', models.CharField(choices=[('январь', 'январь'), ('февраль', 'февраль'), ('март', 'март'), ('апрель', 'апрель'), ('май', 'май'), ('июнь', 'июнь'), ('июль', 'июль'), ('август', 'август'), ('сентябрь', 'сентябрь'), ('октябрь', 'октябрь'), ('ноябрь', 'ноябрь'), ('декабрь', 'декабрь')], max_length=20, verbose_name='месяц рождения')),
                ('year_of_birth', models.IntegerField(verbose_name='год рождения')),
                ('news_and_info', models.BooleanField(verbose_name='новости и информация')),
                ('privacy_policy', models.BooleanField(verbose_name='политика конфиденциальности')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='UserExtended', to=settings.AUTH_USER_MODEL, verbose_name='пользователь')),
            ],
            options={
                'verbose_name': 'дополнительное поле пользователя',
                'verbose_name_plural': 'дополнительные поля пользователей',
            },
        ),
    ]
