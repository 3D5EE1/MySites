from django.contrib import admin

# Register your models here.


from .models import Author, Article


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['surname', 'name', 'city']
    list_filter = ['surname', 'city']
    search_fields = [field.name for field in Author._meta.fields]

    class Meta:
        model = Author


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ['author', 'title']
    list_filter = ['author__surname']
    search_fields = ['author__name', 'author__surname', 'title']

    class Meta:
        model = Article
