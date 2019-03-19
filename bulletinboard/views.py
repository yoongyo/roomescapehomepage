from django.shortcuts import render, get_object_or_404, redirect, reverse, HttpResponse
from .models import Bulletinboard, Comment

import datetime
import os
from django.views.generic import TemplateView
from information.models import Information
from .forms import PostForm, CommentForm

def board_list(request):
    now = datetime.datetime.now()
    info = Information.objects.all()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)

    boardList = Bulletinboard.objects.order_by('-id')[0:20]
    current_page = 1
    totalCnt = Bulletinboard.objects.all().count()


    return render(request, 'board_list.html', {
        'today': nowDate,
        'info': info,
        'board_list': boardList,
        'totalCnt': totalCnt,
        'current_page': current_page,
    }) 

def board_detail(request, pk):

    if request.method =='POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bulletinboard:board_list')
    else:
        form = CommentForm()

    now = datetime.datetime.now()
    info = Information.objects.all()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)
    qs = get_object_or_404(Bulletinboard, pk=pk)
    qs1 = Comment.objects.all()
    return render(request, 'board_detail.html', {
        'form': form,
        'board_detail': qs,
        'comment':qs1,
        'today': nowDate,
        'info': info,
    })

def board_new(request):
    now = datetime.datetime.now()
    info = Information.objects.all()
    nowDate = now.strftime('%Y-%m-%d')
    print(nowDate)

    if request.method =='POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            return redirect(post)
    else:
        form = PostForm()

    return render(request, 'board_new.html', {
        'form': form,
        'today': nowDate,
        'info': info,
    })
