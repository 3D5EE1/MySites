from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def art(request):
    if request.method == 'GET' and 'header-search' in request.GET:
        return HttpResponse(f'123')
    return render(request, 'app_art3d/art3d.html')