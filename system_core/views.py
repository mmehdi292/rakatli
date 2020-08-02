import requests
import random
import json
from django.shortcuts import render
from .models import Video,Khatira,Sound,Sidebar
from .form import SendMailToAdmin
from django.contrib import messages
from random import randrange
from django.db.models import Q
from django.core.paginator import Paginator

# Create your views here.
sidebar = Sidebar.objects.all()
def home(request):
    videos_list = Video.objects.filter().order_by('-date_creation')
    khawatir_list = Khatira.objects.filter().order_by('-date_creation')
    sounds_list = Sound.objects.filter().order_by('-date_creation')
    video_paginator = Paginator(videos_list,5)
    khawatir_paginator = Paginator(khawatir_list,5)
    sounds_paginator = Paginator(sounds_list,5)
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    
    try:
        videos = video_paginator.page(page)
        khawatir = khawatir_paginator.page(page)
        sounds = sounds_paginator.page(page)
    except(EmptyPage, InvalidPage):
        videos = video_paginator.page(video_paginator.num_pages)
        khawatir = khawatir_paginator.page(khawatir_paginator.num_pages)
        sounds = sounds_paginator.page(sounds_paginator.num_pages)


    context = {'last5videos':videos,'last5khawatir':khawatir,'last5sound':sounds,'sidebar':sidebar}
    return render(request, 'system/index.html', context)

def video(request, pk):
    video = Video.objects.get(id=pk)
    video.views += 1
    video.save(update_fields=['views', ])
    more = Video.objects.all().order_by('?')[:6]
    context = {'video':video,'more':more,'sidebar':sidebar}
    return render(request, 'system/video.html', context)

def khawatir(request, pk):
    khawatir = Khatira.objects.get(id=pk)
    khawatir.views += 1
    khawatir.save(update_fields=['views', ])
    more = Khatira.objects.all().order_by('?')[:6]
    context = {'khawatir':khawatir,'more':more,'sidebar':sidebar}
    return render(request, 'system/khawatir.html', context)

def sound(request, pk):
    sound = Sound.objects.get(id=pk)
    sound.views += 1
    sound.save(update_fields=['views', ])
    more = Sound.objects.all().order_by('?')[:6]
    context = {'sound':sound,'more':more,'sidebar':sidebar}
    return render(request, 'system/sounds.html', context)

def all_video(request):
    video = Video.objects.filter().order_by('-date_creation')
    videos_paginator = Paginator(video,15)
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    
    try:
        videos = videos_paginator.page(page)
    except(EmptyPage, InvalidPage):
        videos = videos_paginator.page(videos_paginator.num_pages)

    context = {'videos':videos,'sidebar':sidebar}
    return render(request, 'system/allvideo.html', context)

def all_khawatir(request):
    khawatir = Khatira.objects.filter().order_by('-date_creation')

    khawatirs_paginator = Paginator(khawatir,15)
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    
    try:
        khawatirs = khawatirs_paginator.page(page)
    except(EmptyPage, InvalidPage):
        khawatirs = khawatirs_paginator.page(khawatirs_paginator.num_pages)


    context = {'khawatirs':khawatirs,'sidebar':sidebar}
    return render(request, 'system/allkhawatir.html', context)

def all_sound(request):
    sound = Sound.objects.filter().order_by('-date_creation')

    sounds_paginator = Paginator(sound,15)
    try:
        page = int(request.GET.get('page'))
    except:
        page = 1
    
    try:
        sounds = sounds_paginator.page(page)
    except(EmptyPage, InvalidPage):
        sounds = sounds_paginator.page(sounds_paginator.num_pages)

    context = {'sounds':sounds,'sidebar':sidebar}
    return render(request, 'system/allsound.html', context)

def contact(request):
    form = SendMailToAdmin()
    if request.method == 'POST':

        captcha_token=request.POST.get("g-recaptcha-response")
        cap_url="https://www.google.com/recaptcha/api/siteverify"
        cap_secret="6Ldg77YZAAAAAPcuRdTZIEcK-jvQ7bqGqcPqWHCY"
        cap_data={"secret":cap_secret,"response":captcha_token}
        cap_server_response=requests.post(cap_url,cap_data)
        cap_json=json.loads(cap_server_response.text)
        if cap_json['success']==False:
           messages.error(request, 'اثبت انك لست روبوت')
        else:
            form = SendMailToAdmin(request.POST)
            if form.is_valid():
                form.save()
                messages.success(request, 'لقد ارسال رسالتك بنجاح،سيتم الرد عليك قريبا في بريدك الالكتروني')
            else:
                messages.error(request, 'خطأ في الارسال')
    context = {'form':form,'sidebar':sidebar}
    return render(request, 'system/contact.html', context)

def search(request):
    if request.method == 'POST':
        return render(request, 'system/index.html')
    elif request.method == 'GET':
        videos_list = []
        khawatir_list = []
        sounds_list = []
        value = request.GET['search']
        values = value.split(" ")
        for v in values:
            vs = Video.objects.filter(Q(title__icontains =v) | Q(description__icontains =v)).distinct()
            ks = Khatira.objects.filter(Q(title__icontains=v) | Q(text__icontains =v)).distinct()
            ss = Sound.objects.filter(Q(title__icontains=v) | Q(description__icontains =v)).distinct()
            for v in vs:
                if v not in videos_list:
                    videos_list.append(v)
            for k in ks:
                if k not in khawatir_list:
                    khawatir_list.append(k)
            for s in ss:
                if s not in sounds_list:
                    sounds_list.append(s)

        video_paginator = Paginator(videos_list,5)
        khawatir_paginator = Paginator(khawatir_list,5)
        sounds_paginator = Paginator(sounds_list,5)
        try:
            page = int(request.GET.get('page'))
        except:
            page = 1
        
        try:
            videos = video_paginator.page(page)
            khawatir = khawatir_paginator.page(page)
            sounds = sounds_paginator.page(page)
        except(EmptyPage, InvalidPage):
            videos = video_paginator.page(video_paginator.num_pages)
            khawatir = khawatir_paginator.page(khawatir_paginator.num_pages)
            sounds = sounds_paginator.page(sounds_paginator.num_pages)
        
        context = {'last5videos':videos,'last5khawatir':khawatir,'last5sound':sounds,'sidebar':sidebar,'value':value}
        return render(request, 'system/search.html', context)