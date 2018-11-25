from django.contrib import admin

# Register your models here.

from test_models import models


admin.site.register(models.TestModels)

# admin.site.register(models.Author)
# admin.site.register(models.Book)
#
# admin.site.register(models.Place)
# admin.site.register(models.Restaurant)
# admin.site.register(models.Waiter)
#
# admin.site.register(models.Publication)
# admin.site.register(models.Article)


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'patronymic']
    # list_display = [field.name for field in models.Author._meta.fields]
    list_filter = ['name', 'surname']
    # search_fields = ['surname', 'name']
    search_fields = [field.name for field in models.Author._meta.fields]

    class Meta:
        model = models.Author


admin.site.register(models.Author, AuthorAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'genre', 'text']
    list_filter = ['author']
    search_fields = ['title', 'genre', 'text']

    class Meta:
        model = models.Book


admin.site.register(models.Book, BookAdmin)


class PlaceAdmin(admin.ModelAdmin):
    list_display = ['name', 'address']
    list_filter = ['name']
    search_fields = [field.name for field in models.Place._meta.fields]

    class Meta:
        model = models.Place


admin.site.register(models.Place, PlaceAdmin)


class RestaurantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in models.Restaurant._meta.fields]
    search_fields = ['name']

    class Meta:
        model = models.Restaurant


admin.site.register(models.Restaurant, RestaurantAdmin)


class WaiterAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = [field.name for field in models.Waiter._meta.fields]

    class Meta:
        model = models.Waiter


admin.site.register(models.Waiter, WaiterAdmin)


class PublicationAdmin(admin.ModelAdmin):
    list_display = ['title']
    list_filter = ['title']
    search_fields = [field.name for field in models.Publication._meta.fields]

    class Meta:
        model = models.Publication


admin.site.register(models.Publication, PublicationAdmin)


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['headline']
    list_filter = ['headline']
    search_fields = [field.name for field in models.Article._meta.fields]

    class Meta:
        model = models.Article


admin.site.register(models.Article, ArticleAdmin)




