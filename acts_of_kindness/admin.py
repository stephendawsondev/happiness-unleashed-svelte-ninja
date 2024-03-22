from django.contrib import admin
from .models import ActsOfKindness


@admin.register(ActsOfKindness)
class ActsOfKindnessAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')

   # ordering = ('',)