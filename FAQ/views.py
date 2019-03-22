from django.shortcuts import render
from .models import FAQ

import datetime
from information.models import Information

def FAQs(request):
    now = datetime.datetime.now()
    info = Information.objects.all()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)

    faq = FAQ.objects.all()

    return render(request, 'FAQ.html',{
        'faq': faq,
        'today': nowDate,
        'info': info,
    })