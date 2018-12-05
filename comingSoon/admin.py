from django.contrib import admin
from .models import ComingSoon
# Register your models here.


@admin.register(ComingSoon)
class ComingSoonAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'data_time', 'message']
    list_filter = ['email', ]
    search_fields = [field.name for field in ComingSoon._meta.fields]

    class Meta:
        model = ComingSoon