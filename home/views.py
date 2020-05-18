from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.db import models
import json
# Create your views here.
from blog.models import Blog, Category, Comment
from home.forms import SearchForm, SignUpForm
from home.models import Setting, ContactFormu, ContactFormMessage
from django.contrib.auth import logout, authenticate, login


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
               'randomblogsactive': randomblogsactive,
               # bunu random blog gösterirken div i aktif item olanda kullanıyorum
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
            data.ip = request.META.get('REMOTE_ADDR')
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
               'categorydata': categorydata
               }
    return render(request, 'blogs.html', context)


def blog_detail(request, id, slug):
    category = Category.objects.all()
    blog = Blog.objects.get(pk=id)
    comments = Comment.objects.filter(blog_id=id, status='True')
    context = {
        'category': category,
        'blog': blog,
        'comments': comments
    }
    return render(request, 'blog_detail.html', context)


def blog_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            category = Category.objects.all()
            query = form.cleaned_data['query']
            catid = form.cleaned_data['catid']
            blogs = Blog.objects.filter(title__icontains=query)
            if catid == 0:
                blogs = Blog.objects.filter(title__icontains=query)
            else:
                blogs = Blog.objects.filter(title__icontains=query, category_id=catid)
            context = {'blogs': blogs,
                       'category': category,
                       'query': query,
                       # kelimeyi sayfaya gönderdim, kullanıcının hangi kelimeyi aradığını bilmesi için.
                       }
            return render(request, 'blog_search.html', context)
    return HttpResponseRedirect('/')


def blog_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        blog = Blog.objects.filter(title__icontains=q)
        results = []
        for rs in blog:
            blog_json = {}
            blog_json = rs.city + "," + rs.state
            results.append(blog_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)


def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.error(request, "Hatalı giriş yaptınız. Lütfen kullanıcı adı yada şifrenizi kontrol ediniz..")
            return HttpResponseRedirect('/login')
    category = Category.objects.all()
    context = {'category': category, }
    return render(request, 'login.html', context)


def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    form = SignUpForm()
    category = Category.objects.all()
    context = {'category': category,
               'form': form, }
    return render(request, 'signup.html', context)
