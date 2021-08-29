from django.contrib import admin

from .models import User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

admin.site.register(User, UserAdmin)