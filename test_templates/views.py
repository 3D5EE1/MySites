from django.shortcuts import render
from django.http.response import HttpResponse


# Create your views here.


def main(request):
    return render(request, 'test_templates/_main.html')


def test(request, num='1'):
    if num == '1':
        return HttpResponse(f'вы на 1ой странице книги')
    else:
        return HttpResponse(f'вы на {num} странице книги')


def test_request(request):
    return render(request, "test_templates/test_request.html")


def form(request):
    return HttpResponse(request.POST)


def template(request):
    list1 = [0, 323, 45, 123, 34, 53423, 54, 23]
    context = {
        'test': 'TEXT',
        "list1": list1,
        "name": "Evgeny",
        "surname": "Gurin",
        "coords": {
            "x": '5',
            "y": "y coords",
        },
    }
    return render(request, 'test_templates/template.html', context)


