from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from main.models import Customer, CustomerRequest


class CustomerInline(admin.StackedInline):
    model = Customer
    can_delete = False
    verbose_name_plural = 'employee'


class UserAdmin(BaseUserAdmin):
    inlines = (CustomerInline,)


@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['user', 'ip_data', 'status', 'created']
    list_filter = ['created', 'status']
    search_fields = ['ip_data', 'user__username']


@admin.register(CustomerRequest)
class CustomerRequestAdmin(admin.ModelAdmin):
    list_display = [
        'car_model', 'car_vin', 'car_part_name', 'car_city', 'customer',  'request_type', 'status', 'created'
    ]
    list_filter = ['created', 'status', 'request_type']
    search_fields = ['car_part_name', 'car_vin', 'customer__user__username']


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
