from django.urls import path
from bookings import views

# Urls for all the pages in the bookings app
urlpatterns = [
    path('delivery_request', views.DeliveryBookings.as_view(), name='delivery_request'),
    path('confirmed', views.Confirmed.as_view(), name='confirmed'),
    path('delivery_list', views.DeliveryBookingList.as_view(), name='delivery_list'),
    path('edit_delivery/<int:pk>',
         views.EditDeliveryBooking.as_view(), name='edit_delivery'),
    path('cancel_delivery/<int:pk>',
         views.cancel_delivery_booking, name='cancel_delivery'),
]
