from django.contrib import admin

# Register your models here.

from .models import TestModels, Author, Book, Place, Restaurant, Waiter, Publication, Article


admin.site.register(TestModels)


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'patronymic')
    list_filter = ('surname', 'name', )
    search_fields = [field.name for field in Author._meta.fields]

    class Meta:
        model = Author


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'genre', 'text')
    list_filter = ('author__surname',)
    search_fields = ['title', 'author__surname', 'genre', 'text']

    class Meta:
        model = Book


# -----------------------------------------------------------------------------


@admin.register(Place)
class PlaceAdmin(admin.ModelAdmin):
    list_display = ('name', 'address')
    list_filter = ('name',)
    search_fields = [field.name for field in Place._meta.fields]

    class Meta:
        model = Place


@admin.register(Restaurant)
class RestaurantAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Restaurant._meta.fields]
    search_fields = ('place__name', 'place__address')

    class Meta:
        model = Restaurant


@admin.register(Waiter)
class WaiterAdmin(admin.ModelAdmin):
    list_display = ['name', 'restaurant']
    list_filter = ('name',)
    search_fields = ['name', 'restaurant__place__name']

    class Meta:
        model = Waiter


# -----------------------------------------------------------------------------


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ('title',)
    list_filter = ('title',)
    search_fields = [field.name for field in Publication._meta.fields]

    class Meta:
        model = Publication


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('headline',)
    list_filter = ('headline',)
    search_fields = [field.name for field in Article._meta.fields]

    class Meta:
        model = Article






