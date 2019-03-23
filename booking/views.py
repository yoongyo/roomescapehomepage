from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
import datetime
import sys
sys.path.append('..')

from theme.models import Booking


def booking(request):
    now = datetime.datetime.now()
    nowDate = now.strftime('%Y-%m-%d')
    booking = Booking.objects.all().select_related('theme')
    tobooking = booking.filter(date=nowDate).order_by('-pk')

    return render(request, 'booking/booking.html', {
        'today': nowDate,
        'todaybooking': tobooking,
    })

def booking_list(request):
    booking = Booking.objects.all().select_related('theme').order_by('-date' , '-pk')
    paginator = Paginator(booking, 30)
    page = request.GET.get('page')
    try:
        booking = paginator.page(page)
    except PageNotAnInteger:
        booking = paginator.page(1)
    except EmptyPage:
        booking = paginator.page(paginator.num_pages)
    return render(request, 'booking/booking_list.html', {
        'booking': booking,
    })

