from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import  render, redirect
from .models import Support
from .forms import SupportForm

def support(request):
    message = ''

    if request.method == 'POST':
        form = SupportForm(request.POST)
        if form.is_valid():
            form.save()
            message = 'Сообщение успешно отправлено!'
        else:
            message = 'Ошибка отправления!'

    form = SupportForm()
    return render(request, 'footer/support.html', context={'form': form, 'message': message})
