from django.contrib import admin
from .models import Message
# Register your models here.


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'subject', 'data_time', 'message')
    list_filter = ('email', )
    search_fields = [field.name for field in Message._meta.fields]

    class Meta:
        model = Message