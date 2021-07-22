from django.contrib import admin

# Register your models here.
from authorization.models import EmailAuth

admin.site.register(EmailAuth)