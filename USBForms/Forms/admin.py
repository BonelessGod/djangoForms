from django.contrib import admin

from .models import Inscriptions

# Register your models here.



class InscriptionsAdmin(admin.ModelAdmin):
    list_display = ('firstName', 'lastName', 'email')


admin.site.register(Inscriptions, InscriptionsAdmin)