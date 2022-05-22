from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import TracksForm, UserEditForm, AvatarsForm
from .models import Tracks, Avatars
from django.contrib.auth.models import User
from django.contrib import messages

def clear_messages(request):
    storage = messages.get_messages(request)
    storage.used = True

def profile(request):
    message = ''
    message_error = ''

    if request.method == 'POST':
        form = TracksForm(request.POST, request.FILES)
        if form.is_valid():
            print(request.user)
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            message = 'Успешно!'
        else:
            message_error = 'Некорректный формат, пожалуйста, используйте .mp3 или .wav'

    form = TracksForm()
    tracks = Tracks.objects.filter(user=request.user)
    image = Avatars.objects.filter(user=request.user)
    return render(request, 'userprofile/profile.html', context={'form': form, 'message': message, 'message_error': message_error, 'tracks': tracks, 'image': image})


def edit(request):
    if request.method == 'POST':
        form_img = AvatarsForm(request.POST, request.FILES)
        form = UserEditForm(request.POST, instance=request.user)
        form.actual_user = request.user

        if form_img.is_valid():
            print(request.user)
            obj = form_img.save(commit=False)
            obj.user = request.user
            obj.save()

        if form.is_valid():
            form.save()
            clear_messages(request)
            for field in form.errors:
                for error in form[field].errors:
                    messages.error(request, error)
        else:
            clear_messages(request)

    form = UserEditForm()
    form_img = AvatarsForm()
    image = Avatars.objects.filter(user=request.user)
    return render(request, 'userprofile/edit.html', context={'form': form, 'form_img': form_img, 'image': image})
