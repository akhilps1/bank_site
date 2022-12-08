from django.contrib import admin
from .models import AccountForm,FormSubmitted

# Register your models here.

admin.site.register(AccountForm)
admin.site.register(FormSubmitted)