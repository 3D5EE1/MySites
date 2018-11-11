from django.shortcuts import render

# Create your views here.


def aboutMe(request):
    return render(request, 'aboutMe/aboutMe.html')