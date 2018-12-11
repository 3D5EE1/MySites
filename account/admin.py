from django.contrib import admin
from .models import UserExtended
# Register your models here.


@admin.register(UserExtended)
class UserExtendedAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'user', 'country_list', 'news_and_info', 'privacy_policy')
    list_filter = ('user__email', 'user__username')
    search_fields = ('user__email', 'user__username', 'country_list')

    class Meta:
        model = UserExtended
