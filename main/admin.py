from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe

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
        'request_type', 'car_model_b', 'car_vin', 'car_part_name', 'car_city', 'customer_name', 'customer', 'status', 'created'
    ]
    list_display_links = ('request_type', 'car_model_b')
    list_filter = ['created', 'status', 'request_type']
    search_fields = ['car_part_name', 'car_vin', 'customer__user__username']

    def car_model_b(self, obj):
        return mark_safe('<b>%s</b>' % obj.car_model)
    car_model_b.short_description = 'Car Model'
    car_model_b.allow_tags = True


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
