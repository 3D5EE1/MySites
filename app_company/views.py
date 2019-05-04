from django.shortcuts import render

# Create your views here.


def company_it_one_page(request):
    return render(request, 'app_company/company-it-one-page.html')


def company_it_domain(request):
    return render(request, 'app_company/company-it-domain.html')
