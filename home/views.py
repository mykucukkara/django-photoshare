from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import models

# Create your views here.
from blog.models import Blog, Category
from home.models import Setting, ContactFormu, ContactFormMessage


def index(request):
    setting = Setting.objects.get(pk=1)
    sliderdata = Blog.objects.all()[:4]
    category = Category.objects.all()
    dayblogs = Blog.objects.all()[:3]
    lastblogs = Blog.objects.all().order_by('-id')[:3]
    randomblogsactive = Blog.objects.all().order_by('?')[:1]
    randomblogs = Blog.objects.all().order_by('?')[:3]

    context = {'setting': setting,
               'page': 'home',
               'sliderdata': sliderdata,
               'category': category,
               'dayblogs': dayblogs,
               'lastblogs': lastblogs,
               'randomblogsactive': randomblogsactive, #bunu random blog gösterirken div i aktif item olanda kullanıyorum
               'randomblogs': randomblogs}
    return render(request, 'index.html', context)


def hakkimizda(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting,
               'category': category}
    return render(request, 'hakkimizda.html', context)


def referanslar(request):
    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    context = {'setting': setting, 'category': category}
    return render(request, 'referanslarimiz.html', context)


def iletisim(request):
    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMessage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür ederiz.")
            return HttpResponseRedirect('/iletisim')
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    form = ContactFormu()
    context = {'setting': setting, 'form': form, 'category': category}
    return render(request, 'iletisim.html', context)


def category_blogs(request, id, slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    blogs = Blog.objects.filter(category_id=id)
    context = {'blogs': blogs,
               'category': category,
               'categorydata' : categorydata
               }
    return render(request, 'blogs.html', context)
