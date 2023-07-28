from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Restaurant first sitting at noon and last sitting 11pm
time_slots = (
    ('12:00', '12:00'),
    ('13:00', '13:00'),
    ('14:00', '14:00'),
    ('15:00', '15:00'),
    ('16:00', '16:00'),
    ('17:00', '17:00'),
    ('18:00', '18:00'),
    ('19:00', '19:00'),
    ('20:00', '20:00'),
    ('21:00', '21:00'),
    ('22:00', '22:00'),
    ('23:00', '23:00'),
)

delivery_options = (
    ('Standard/Basic Delivery', 'Standard/Basic Delivery'),
    ('Expedited Delivery', 'Expedited Delivery'),
    ('Premium Delivery', 'Premium Delivery'),
    ('White Glove/Platinum Delivery', 'White Glove/Platinum Delivery'),
)


# Status options inspired by the JustEat status' when ordering
status_options = (
    ('Awaiting confirmation', 'Awaiting Confirmation'),
    ('Booking Confirmed', 'Booking Confirmed'),
    ('Booking Rejected', 'Booking Rejected'),
    ('Booking Expired', 'Booking Expired'),
)


# The service model for the database


class Service(models.Model):
    """
    a class for the Service model
    """
    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(
        max_length=50,
        #choices=delivery_options,
        default='Standard/Basic Delivery',
        unique=True
        )
    # max_seats = models.PositiveIntegerField(default=2)

    class Meta:
        ordering = ['service_name']

    def __str__(self):
        return self.service_name


# The booking model for the database


class Booking(models.Model):
    """
    a class for the Booking model
    """
    booking_id = models.AutoField(primary_key=True)
    created_date = models.DateTimeField(auto_now_add=True)
    requested_date = models.DateField()
    requested_time = models.CharField(
        max_length=200,
        choices=time_slots,
        default='17:00'
        )
    service = models.ForeignKey(
        Service,
        on_delete=models.CASCADE,
        #choices=delivery_options,
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
        default='awaiting confirmation'
        )

    class Meta:
        ordering = ['-requested_time']
        unique_together = ('requested_date', 'requested_time', 'service')

    def __str__(self):
        return self.status
