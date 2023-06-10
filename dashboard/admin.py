
from django.contrib import admin
from .models import Address, Dashboard,History

# Register your models here.
admin.site.register(Dashboard)

admin.site.register(History)

admin.site.register(Address)