from django.shortcuts import render

# Create your views here.




def detective(request):
    return render(request, 'detective/detective.html')