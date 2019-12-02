from __future__ import unicode_literals
from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from .models import *
from .forms import *



def index(request):
    try:
        if not request.user.is_authenticated:
            return redirect('/accounts/login/')
        current_user=request.user
        profile =Profile.objects.get(username=current_user)
    except ObjectDoesNotExist:
        return redirect('create-profile')

    return render(request,'index.html')

@login_required(login_url='/accounts/login/')
def create_profile(request):
    current_user=request.user
    if request.method=="POST":
        form =ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()
        return HttpResponseRedirect('/')

    else:

        form = ProfileForm()
    return render(request,'profile_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def update_profile(request):
    current_user=request.user
    if request.method=="POST":
        instance = Profile.objects.get(username=current_user)
        form =ProfileForm(request.POST,request.FILES,instance=instance)
        if form.is_valid():
            profile = form.save(commit = False)
            profile.username = current_user
            profile.save()

        return redirect('Index')

    elif Profile.objects.get(username=current_user):
        profile = Profile.objects.get(username=current_user)
        form = ProfileForm(instance=profile)
    else:
        form = ProfileForm()

    return render(request,'update_profile.html',{"form":form})

@login_required(login_url='/accounts/login/')
def authorities(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    authorities = Authorities.objects.filter(hood=profile.hood)

    return render(request,'authorities.html',{"authorities":authorities})

@login_required(login_url='/accounts/login/')
def businesses(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    businesses = Business.objects.filter(hood =profile.hood)

    return render(request,'businesses.html',{"businesses":businesses})

@login_required(login_url='/accounts/login/')
def health(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    healthservices = Health.objects.filter(hood=profile.hood)

    return render(request,'health.html',{"healthservices":healthservices})

@login_required(login_url='/accounts/login/')
def notification(request):
    current_user=request.user
    profile=Profile.objects.get(username=current_user)
    all_notifications = notifications.objects.filter(hood=profile.hood)

    return render(request,'notifications.html',{"notifications":all_notifications})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =BusinessForm(request.POST,request.FILES)
        if form.is_valid():
            business = form.save(commit = False)
            business.owner = current_user
            business.hood = profile.hood
            business.save()

        return HttpResponseRedirect('/businesses')

    else:
        form = BusinessForm()

    return render(request,'business_form.html',{"form":form})


@login_required(login_url='/accounts/login/')
def new_notification(request):
    current_user=request.user
    profile =Profile.objects.get(username=current_user)

    if request.method=="POST":
        form =notificationsForm(request.POST,request.FILES)
        if form.is_valid():
            notification = form.save(commit = False)
            notification.author = current_user
            notification.hood = profile.hood
            notification.save()

            return HttpResponseRedirect('/notifications')


    else:
        form = notificationsForm()

    return render(request,'notification_form.html',{"form":form})

@login_required(login_url='/accounts/login/')
def search_results(request):
    return