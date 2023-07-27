from django.shortcuts import render, reverse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator

from .models import Booking
from .forms import BookingForm


def get_user_instance(request):
    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user

class DeliveryBookings(View):
    template_name = 'bookings/delivery_request.html'
    success_message = 'Booking has been made.'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, 'bookings/delivery_request.html',
                      {'booking_form': booking_form})

    def post(self, request):
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            delivery_booking = booking_form.save(commit=False)
            delivery_booking.user = request.user
            delivery_booking.save()
            messages.success(
                request, "Booking successful, awaiting confirmation")
            return render(request, 'bookings/confirmed.html')

        return render(request, 'bookings/delivery_request.html',
                      {'booking_form': booking_form})

class Confirmed(generic.DetailView):
    template_name = 'bookings/confirmed.html'

    def get(self, request):
        return render(request, 'bookings/confirmed.html')

class DeliveryBookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'delivery_list.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):

        delivery_booking = Booking.objects.all()
        paginator = Paginator(Booking.objects.filter(user=request.user), 4)
        page = request.GET.get('page')
        delivery_booking_page = paginator.get_page(page)
        today = datetime.datetime.now().date()

        for date in delivery_booking:
            if date.delivery_date < today:
                date.status = 'Booking Expired'

        if request.user.is_authenticated:
            delivery_bookings = Booking.objects.filter(user=request.user)
            return render(
                request,
                'bookings/delivery_list.html',
                {
                    'delivery_booking': delivery_booking,
                    'delivery_bookings': delivery_bookings,
                    'delivery_booking_page': delivery_booking_page})
        else:
            return redirect('accounts/login.html')

class EditDeliveryBooking(SuccessMessageMixin, UpdateView):
    model = Booking
    form_class = BookingForm
    template_name = 'bookings/edit_delivery.html'
    success_message = 'Booking has been updated.'

    def get_success_url(self, **kwargs):
        return reverse('delivery_list')

def cancel_delivery_booking(request, pk):
    delivery_booking = Booking.objects.get(pk=pk)

    if request.method == 'POST':
        delivery_booking.delete()
        messages.success(request, "Booking cancelled")
        return redirect('delivery_list')

    return render(
        request, 'bookings/cancel_delivery.html', {'delivery_booking': delivery_booking})
