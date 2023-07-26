# Imports
from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import DeliveryService, Booking

@admin.register(DeliveryService)
class DeliveryServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'service_type', 'delivery_time')

@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
        'service_type',
        'status',
        'service_id',
        'requested_date',
        'requested_time',
        'created_date'
        )
    list_display = (
        'booking_id',
        'user',
        'name',
        'phone',
        'service_type',
        'status',
        'delivery_service',
        'requested_date',
        'requested_time',
        'created_date')

    search_fields = ['user__name']
    list_filter = (('requested_date', DateRangeFilter),)
    actions = ['confirm_bookings']

    def confirm_bookings(self, request, queryset):
        queryset.update(status='Booking Confirmed')
