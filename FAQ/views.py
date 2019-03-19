from django.shortcuts import render
from .models import Qna

import datetime
from information.models import Information

def FAQs(request):
    now = datetime.datetime.now()
    info = Information.objects.all()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)

    qs =  Qna.objects.all()

    return render(request, 'FAQ.html',{
        'FAQ_list': qs,
        'today': nowDate,
        'info': info,
    })