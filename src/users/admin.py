from django.contrib import admin

from .models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'phone_number', 'website']
    list_display_links = ['user', 'phone_number']
    list_editable = ['website']

    search_fields = [
        'user',
        'user__first_name',
        'user__email',
        'phone_number',
    ]

    list_filter = ['user__is_staff']

#admin.site.register(Profile, ProfileAdmin)