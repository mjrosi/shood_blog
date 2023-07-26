from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Delivery options
delivery_options = (
    ('Standard/Basic Delivery', 'Standard/Basic Delivery'),
    ('Expedited Delivery', 'Expedited Delivery'),
    ('Premium Delivery', 'Premium Delivery'),
    ('White Glove/Platinum Delivery', 'White Glove/Platinum Delivery'),
)

# Status options
status_options = (
    ('Awaiting confirmation', 'Awaiting Confirmation'),
    ('Booking Confirmed', 'Booking Confirmed'),
    ('Booking Rejected', 'Booking Rejected'),
    ('Booking Expired', 'Booking Expired'),
)

# The DeliveryService model for the database
class DeliveryService(models.Model):
    """
    a class for the DeliveryService model
    """
    service_id = models.AutoField(primary_key=True)
    service_type = models.CharField(max_length=50)
    delivery_time = models.TimeField()
    service_name = models.CharField(
        max_length=50,
        choices=delivery_options,
        default='Standard/Basic Delivery'
        )

    class Meta:
        ordering = ['service_name']

    def __str__(self):
        return self.service_name

# The Booking model for the database
class Booking(models.Model):
    """
    a class for the Booking model
    """
    booking_id = models.IntegerField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    delivery_date = models.DateField()
    service_type = models.CharField(max_length=50)
    delivery_service = models.ForeignKey(DeliveryService, on_delete=models.CASCADE)
    requested_date = models.DateField()
    requested_time = models.TimeField()
    service = models.ForeignKey(
        DeliveryService,
        on_delete=models.CASCADE,
        related_name="service_reserved",
        null=True
        )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user", null=True)
    name = models.CharField(
        max_length=50,
        null=True
        )
    email = models.EmailField(
        max_length=254,
        default=""
        )
    phone = PhoneNumberField(null=True)
    status = models.CharField(
        max_length=25,
        choices=status_options,
        default='Awaiting confirmation'
        )

    class Meta:
        ordering = ['-delivery_date']

    def __str__(self):
        return self.status

