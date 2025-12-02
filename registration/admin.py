from django.contrib import admin
from .models import UserRegistration

# Define how the table looks in the Admin Panel
class UserRegistrationAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email') # Columns to show
    search_fields = ('first_name', 'last_name', 'email')       # Enable search bar

# Register the model with the customized view
admin.site.register(UserRegistration, UserRegistrationAdmin)