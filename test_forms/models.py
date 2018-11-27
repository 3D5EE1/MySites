from django.db import models

# Create your models here.


class Author(models.Model):
    CHOICES_FOR_CITY = (
        ('москва', 'москва'),
        ('санкт-питербург', 'санкт-питербург'),
        ('екатеринбург', 'екатеринбург'),
        ('казань', 'казань'),
    )

    name = models.CharField(max_length=200, verbose_name="Имя автора")
    surname = models.CharField(max_length=200, verbose_name='Фамилия автора')
    city = models.CharField(choices=CHOICES_FOR_CITY, max_length=200, blank=True, verbose_name="Город",
                            help_text='Выберите город из списка ')

    def __str__(self):
        return f'{self.surname} {self.name}'

    class Meta:
        verbose_name_plural = "Авторы"
        verbose_name = 'Автор'


class Article(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name="Автор статьи")
    title = models.CharField(max_length=100, verbose_name="Заголовок")
    text = models.TextField(max_length=500, verbose_name='Текст статьи')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = 'Статья'

