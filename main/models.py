from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    class Status(models.TextChoices):
        NEW = 'NW', 'New'
        BANNED = 'BN', 'Banned'
        SUCCESSFUL = 'SC', 'Successful Customer'

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    ip_data = models.CharField(max_length=32, blank=True, default="")
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.NEW)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.user}/{self.status}'


class CustomerRequest(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'DF', 'Draft'
        ON_WORK = 'OW', 'On work'
        DONE = 'DN', 'Done'

    car_model = models.CharField(max_length=32, blank=True, default="")
    car_vin = models.CharField(max_length=32, blank=True, default="")
    car_part_name = models.CharField(max_length=64, blank=True, default="")
    additional_info = models.CharField(max_length=128, blank=True, default="")

    customer = models.ForeignKey(Customer, related_name='customer_requests', on_delete=models.CASCADE)

    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=2, choices=Status.choices, default=Status.DRAFT)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return f'{self.customer}; {self.car_vin}/{self.car_part_name}'
