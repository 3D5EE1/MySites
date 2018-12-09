from django.contrib import admin
from .models import UserExtended
# Register your models here.


@admin.register(UserExtended)
class UserExtendedAdmin(admin.ModelAdmin):
    list_display = ('__str__', )
    list_filter = ('user__email', 'user__username')
    search_fields = ('__str__', 'user__first_name', 'user__last_name')

    class Meta:
        model = UserExtended
