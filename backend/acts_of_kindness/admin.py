from django.contrib import admin
from .models import ActsOfKindness


@admin.register(ActsOfKindness)
class ActsOfKindnessAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'approved')
    list_filter = ('approved',)
    actions = ['approve_acts']

    def approve_acts(self, request, queryset):
        queryset.update(approved=True)

    approve_acts.short_description = 'Approve selected acts of kindness'

   # ordering = ('',)
