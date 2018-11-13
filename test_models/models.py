from django.db import models

# Create your models here.


class TestModels(models.Model):
    integer_field = models.IntegerField()
    positive_field = models.PositiveIntegerField()
    positive_small_field = models.PositiveSmallIntegerField()
    big_integer_field = models.BigIntegerField()
    float_field = models.FloatField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=5)
    text_field = models.TextField(max_length=20)
    data_field = models.DateField(auto_now=True)
    data_time_field = models.DateTimeField(auto_now_add=True)
    decimal_field = models.DecimalField(max_digits=8, decimal_places=2)
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='files')
    image_field = models.ImageField(upload_to='images')