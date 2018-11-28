# Generated by Django 2.1.3 on 2018-11-27 23:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Заголовок')),
                ('text', models.TextField(max_length=500, verbose_name='Текст статьи')),
            ],
            options={
                'verbose_name': 'Статья',
                'verbose_name_plural': 'Статьи',
            },
        ),
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, verbose_name='Имя автора')),
                ('surname', models.CharField(max_length=200, verbose_name='Фамилия автора')),
                ('city', models.CharField(blank=True, choices=[('москва', 'москва'), ('санкт-питербург', 'санкт-питербург'), ('екатеринбург', 'екатеринбург'), ('казань', 'казань')], help_text='Выберите город из списка ', max_length=200, verbose_name='Город')),
            ],
            options={
                'verbose_name': 'Автор',
                'verbose_name_plural': 'Авторы',
            },
        ),
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='test_forms.Author', verbose_name='Автор статьи'),
        ),
    ]
