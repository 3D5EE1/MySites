from django.contrib import admin
from .models import User, UserExtended

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('email', 'is_active')
    list_filter = ('email', 'is_active')
    search_fields = ('email', )

    class Meta:
        model = User


@admin.register(UserExtended)
class UserExtendedAdmin(admin.ModelAdmin):
    list_display = ('country_list', 'news_and_info', 'privacy_policy')
    list_filter = ('user__email', )
    search_fields = ('user__email', 'country_list')

    class Meta:
        model = UserExtended


# @admin.register(UserExtended)
# class UserExtendedAdmin(admin.ModelAdmin):
#     list_display = ('__str__', 'user', 'country_list', 'news_and_info', 'privacy_policy')
#     list_filter = ('user__email', 'user__username')
#     search_fields = ('user__email', 'user__username', 'country_list')
#
#     class Meta:
#         model = UserExtended
