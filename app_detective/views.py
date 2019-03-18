from django.shortcuts import render

# Create your views here.




def detective(request):
    return render(request, 'app_detective/detective.html')