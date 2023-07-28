from django.contrib import admin
from rangefilter.filters import DateRangeFilter
from .models import Service, Booking

# Registration of tables to display in the admin panel
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('service_id', 'service_name')


# Registration of bookings to display in the admin panel
@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_filter = (
        'user',
        'name',
        'email',
        'phone',
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
        'status',
        'service',
        'requested_date',
        'requested_time',
        'created_date')

    search_fields = ['guest__name']
    list_filter = (('requested_date', DateRangeFilter),)
    actions = ['confirm_bookings']

    def confirm_bookings(self, request, queryset):
        queryset.update(status='Booking Confirmed')
