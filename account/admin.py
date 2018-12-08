from django.contrib import admin
from .models import Account
# Register your models here.


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    list_filter = ('user__email', 'user__username')
    search_fields = ('__str__', 'user__first_name', 'user__last_name')

    class Meta:
        model = Account