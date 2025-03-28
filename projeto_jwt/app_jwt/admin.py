from django.contrib import admin
from .models import Username
from django.contrib.auth.admin import UserAdmin

# Register your models here.

class UsernameAdmin(UserAdmin):
    list_display = ('username', 'email', 'telefone', 'cpf', 'endereco')

    fieldsets = UserAdmin.fieldsets + (
        (None, {'fields':('telefone', 'cpf', 'endereco')}),
    )

    add_fieldsets = UserAdmin.add_fieldsets + (
        (None, {'fields':('telefone', 'cpf', 'endereco')}),
    )

admin.site.register(Username, UsernameAdmin)