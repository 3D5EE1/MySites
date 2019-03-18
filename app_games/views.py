from django.shortcuts import render


# Create your views here.

def games(request):
    return render(request, 'app_games/games.html')
