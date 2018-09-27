from django.shortcuts import render

# Create your views here.


def art(request):
    return render(request, 'art3d/art3d.html')