from django.shortcuts import render
from django.http import HttpResponse
from userprofile.models import Tracks
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

def index(request):
    query = request.GET.get('search')

    if query:
        return render(request, 'main/search.html', context={"tracks": Tracks.objects.filter(track_name__contains=query), 'query': query})
    else:
        tracks = Tracks.objects.order_by('?')[:3]
        charts_ = Tracks.objects.order_by('-auditions')[:4]
        return render(request, 'main/index.html', context={'tracks': tracks, 'charts': charts_})

def recommends(request):
    query = request.GET.get('search')

    if query:
        return render(request, 'main/search.html', context={"tracks": Tracks.objects.filter(track_name__contains=query), 'query': query})
    else:
        tracks = Tracks.objects.order_by('?')
        return render(request, 'main/recommends.html', context={'tracks': tracks})

def charts(request):
    query = request.GET.get('search')

    if query:
        return render(request, 'main/search.html', context={"tracks": Tracks.objects.filter(track_name__contains=query), 'query': query})
    else:
        charts_ = Tracks.objects.order_by('-auditions')
        return render(request, 'main/charts.html', context={'charts': charts_})

@csrf_exempt
def addlisten(request):
    if request.method == 'POST':
        au_id = request.POST.get('audio_id', None)
        audit = Tracks.objects.get(id=au_id)
        audit.auditions += 1
        audit.save()

    return JsonResponse({})
