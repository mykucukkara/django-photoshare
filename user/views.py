from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from blog.models import Category, Comment, Blog, BlogForm
from home.models import UserProfile
from user.forms import UserUpdateForm, ProfileUpdateForm


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {'category': category,
               'profile': profile}
    return render(request, 'user_profile.html', context)


@login_required(login_url='/login')  # login kontrol
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated!')
            return redirect('/user')
    else:
        category = Category.objects.all()
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        context = {'category': category,
                   'profile_form': profile_form,
                   'user_form': user_form}
        return render(request, 'user_update.html', context)


@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password was succesfully updated!')
            # return redirect('/user')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error below.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        return render(request, 'change_password.html', {
            'form': form, 'category': category
        })


@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    context = {'category': category, 'comments': comments, }
    return render(request, 'user_comments.html', context)


@login_required(login_url='/login')
def deletecomment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Comment deleted..')
    return HttpResponseRedirect('/user/comments')


@login_required(login_url='/login')  # check login
def myblogs(request):
    category = Category.objects.all()
    current_user = request.user
    myblogs = Blog.objects.filter(user_id=current_user.id)
    context = {'category': category,
               'myblogs': myblogs, }
    return render(request, 'user_myblogs.html', context)


@login_required(login_url='/login')
def addblog(request):
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            current_user = request.user
            data = Blog()
            data.user_id = current_user.id
            data.title = form.cleaned_data['title']
            data.keywords = form.cleaned_data['keywords']
            data.description = form.cleaned_data['description']
            data.image = form.cleaned_data['image']
            data.category = form.cleaned_data['category']
            data.slug = form.cleaned_data['slug']
            data.detail = form.cleaned_data['detail']
            data.status = 'False'
            data.save()
            messages.success(request, 'Your Blog Inserted Successfuly')
            return HttpResponseRedirect('/user/myblogs')
        else:
            messages.success(request, 'Blog Form Error :' + str(form.errors))
            return HttpResponseRedirect('/user/addblog')
    else:
        category = Category.objects.all()
        form = BlogForm()
        context = {
            'category': category,
            'form': form,
        }
        return render(request, 'user_addblog.html', context)


@login_required(login_url='/login')  # check login
def editblog(request, id):
    blog = Blog.objects.get(id=id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=blog)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your blog updated successfuly!')
            return HttpResponseRedirect('/user/myblogs')
        else:
            messages.error(request, 'Content Form Error: ' + str(form.errors))
            return HttpResponseRedirect('/user/editblog/' + str(id))
    else:
        category = Category.objects.all()
        form = BlogForm(instance=blog)
        context = {'category': category,
                   'form': form}
    return render(request, 'user_editblog.html', context)




@login_required(login_url='/login')  # check login
def deleteblog(request, id):
    current_user = request.user
    Blog.objects.filter(id=id, user_id=current_user.id, ).delete()
    messages.success(request, 'Blog deleted...')
    return HttpResponseRedirect('/user/myblogs')
