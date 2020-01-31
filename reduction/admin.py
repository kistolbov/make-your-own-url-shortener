from django.contrib import admin
from reduction.models import URL


class Admin(admin.ModelAdmin):
    list = ('short_id', 'url', 'public_date', 'counter')
    ordering = ('-public_date', )


admin.site.register(URL, Admin)
