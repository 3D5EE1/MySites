from django.shortcuts import render

# Create your views here.


def tattoo(request):
    return render(request, 'tattoo/tattoo.html')