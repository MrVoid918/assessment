from django.contrib import admin
from django.shortcuts import render
from .models import Claims
from django.contrib import messages
# Register your models here.


class ClaimsAdmin(admin.ModelAdmin):

    list_display = ['name', 'claim_status']
    actions = ['approve']

    @admin.action(description="Update status to Accepted")
    def approve(self, request, queryset):
        queryset.update(claim_status='AC')
        self.message_user(request, "Claim Approved", messages.SUCCESS)


admin.site.register(Claims, ClaimsAdmin)
