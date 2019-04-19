from django.shortcuts import render

# Create your views here.


def company(request):
    return render(request, 'app_company/company.html')


def company_jino1(request):
    return render(request, 'app_company/company-1.html')
