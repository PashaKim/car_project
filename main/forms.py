from datetime import date

from django import forms
from django.contrib.auth.models import User

from car_project.settings import MAX_PAST_REQUESTS, IS_SEND_EMAIL
from car_project.utils import send_email_to_admin
from main.models import Customer, CustomerRequest


class CustomerRequestForm(forms.Form):

    def __init__(self, ip_value=None, *args, **kwargs):
        self.ip_value = ip_value
        super().__init__(*args, **kwargs)

    name = forms.CharField(max_length=32)
    phone = forms.CharField(max_length=32)
    car_model = forms.CharField(max_length=32)
    vin_code = forms.CharField(max_length=32, required=False)
    part_name = forms.CharField(max_length=128, required=False)
    car_city = forms.CharField(max_length=128, required=False)
    additional_info = forms.CharField(max_length=256, required=False)
    request_type = forms.CharField(max_length=32, required=False)

    def save(self):
        customer = Customer.objects.filter(ip_data=self.ip_value).first()

        if customer and customer.status == Customer.Status.BANNED:
            return None

        if not customer:
            user = self.create_user()
            customer = self.create_customer(user)

        past_requests = CustomerRequest.objects.filter(customer=customer, created__date=date.today())

        if len(past_requests) >= MAX_PAST_REQUESTS:
            customer.status = Customer.Status.BANNED
            customer.save()
            return None

        instance = CustomerRequest.objects.create(
            customer=customer,
            car_model=self.cleaned_data.get('car_model', ''),
            car_vin=self.cleaned_data.get('vin_code', ''),
            car_part_name=self.cleaned_data.get('part_name', ''),
            car_city=self.cleaned_data.get('car_city', ''),
            request_type=self.cleaned_data.get('request_type', ''),
            additional_info=self.cleaned_data.get('additional_info', ''),
        )
        if IS_SEND_EMAIL:
            send_email_to_admin(instance)

        return instance

    def create_user(self):
        user, created = User.objects.get_or_create(
            username=self.cleaned_data.get('phone', 'anon'),
            first_name=self.cleaned_data.get('name'),
        )
        return user

    def create_customer(self, user: User):
        customer = Customer.objects.filter(user_id=user.id).first()
        if not customer:
            customer = Customer.objects.create(user_id=user.id, ip_data=self.ip_value)
        return customer
