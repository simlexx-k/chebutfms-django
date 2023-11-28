from django.contrib import admin

# Register your models here.
from .models import Farmer
from django.apps import apps

admin.site.site_header = 'Chebut Tea Farmer Management System'
admin.site.site_title = 'Ukulima Bora'

from django.contrib import admin
from .models import Payment

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['farmer', 'monthly_period', 'amount_paid']
    actions = ['recalculate_payments']

    def recalculate_payments(self, request, queryset):
        for payment in queryset:
            payment.save()

    recalculate_payments.short_description = "Recalculate selected payments"

admin.site.register(Payment, PaymentAdmin)

fms_models = apps.get_app_config('fms').get_models()

for model in fms_models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass