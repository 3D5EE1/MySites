from django.db import models

# Create your models here.


class TestModels(models.Model):
    integer_field = models.IntegerField(verbose_name='integer')
    positive_field = models.PositiveIntegerField(verbose_name='positive')
    positive_small_field = models.PositiveSmallIntegerField(verbose_name='positive small')
    big_integer_field = models.BigIntegerField(verbose_name='big integer')
    float_field = models.FloatField(verbose_name='float')
    binary_field = models.BinaryField(verbose_name='binary')
    boolean_field = models.BooleanField(verbose_name='boolean')
    char_field = models.CharField(max_length=5, verbose_name='char')
    text_field = models.TextField(max_length=20, blank=True, verbose_name='text')
    data_field = models.DateField(auto_now=False, verbose_name='data')
    data_time_field = models.DateTimeField(auto_now_add=False, verbose_name='data time')
    decimal_field = models.DecimalField(max_digits=8, decimal_places=2, verbose_name='decimal')
    email_field = models.EmailField(verbose_name='email')
    file_field = models.FileField(upload_to='files', blank=True, verbose_name='file')
    image_field = models.ImageField(upload_to='images', blank=True, verbose_name='image')

    def __str__(self):
        return f'{self.text_field} {self.email_field}'

    class Meta:
        verbose_name_plural = 'Примеры полей'
        verbose_name = "Пример полей"


# -----------------------------------------------------------------------------


class Author(models.Model):
    name = models.CharField(max_length=50, verbose_name="имя автора")
    patronymic = models.CharField(max_length=50, verbose_name="отчество автора")
    surname = models.CharField(max_length=50, verbose_name="фамилия автора")
    date_birth = models.DateField(auto_now=False, verbose_name="дата рождения")

    def __str__(self):
        return f'{self.surname} {self.name} {self.patronymic}'

    class Meta:
        verbose_name_plural = 'Авторы'
        verbose_name = "Автор"


class Book(models.Model):
    CHOICE_GENRE = (
        ('комедия', 'комедия'),
        ('трагедия', 'трагедия'),
        ('драма', 'драма')
    )

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='автор книги')
    title = models.CharField(max_length=50, verbose_name='название книги')
    text = models.TextField(max_length=1000, blank=True, verbose_name='текст')
    genre = models.CharField(max_length=50, choices=CHOICE_GENRE, default='драма', verbose_name='жанр')

    def __str__(self):
        return f'{self.title} ... {self.author.name[0]}. {self.author.patronymic[0]}. {self.author.surname}'

    class Meta:
        verbose_name_plural = 'Книги'
        verbose_name = "Книга"


# -----------------------------------------------------------------------------


class Place(models.Model):
    name = models.CharField(max_length=50, verbose_name='название ресторана')
    address = models.CharField(max_length=80, verbose_name='адрес ресторана')

    def __str__(self):
        return f'ресторан {self.name}, по адресу {self.address}'

    class Meta:
        verbose_name_plural = 'Адреса ресторанов'
        verbose_name = "Адрес ресторана"


class Restaurant(models.Model):
    place = models.OneToOneField(Place, on_delete=models.CASCADE, verbose_name='адрес ресторана')
    serves_hot_dogs = models.BooleanField(default=False, verbose_name='заказ хот догов')
    serves_pizza = models.BooleanField(default=False, verbose_name='заказ пиццы')
    serves_steak = models.BooleanField(default=False, verbose_name='заказ стайков')
    serves_burgers = models.BooleanField(default=False, verbose_name='заказ бургеров')

    def __str__(self):
        return f'{self.place.name}'

    class Meta:
        verbose_name_plural = 'Рестораны'
        verbose_name = "Ретсоран"


class Waiter(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, verbose_name='название ресторана')
    name = models.CharField(max_length=100, verbose_name='имя официанта')

    def __str__(self):
        return f'{self.name}, {self.restaurant.place}'

    class Meta:
        verbose_name_plural = 'Официанты'
        verbose_name = "Официант"


# -----------------------------------------------------------------------------


class Publication(models.Model):
    title = models.CharField(max_length=30, verbose_name='название газеты')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Газеты'
        verbose_name = "Газета"
        ordering = ['title']


class Article(models.Model):
    headline = models.CharField(max_length=50, verbose_name='заголовок статьи')
    publication = models.ManyToManyField(Publication, verbose_name='публикация')

    def __str__(self):
        return self.headline

    class Meta:
        verbose_name_plural = 'Статьи'
        verbose_name = "Статья"
        ordering = ['headline']








