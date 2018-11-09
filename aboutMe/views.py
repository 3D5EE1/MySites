from django.shortcuts import render

# Create your views here.


def aboutMe(request):
    return render(request, 'aboutMe/aboutMe.html')


def main(request):
    return render(request, 'aboutMe/_main.html')


from django.http.response import HttpResponse


def test(request, num='1'):
    if num == '1':
        return HttpResponse(f'вы на 1ой странице книги')
    else:
        return HttpResponse(f'вы на {num} странице книги')


def test_request(request):
    return render(request, "aboutMe/test_request.html")


def form(request):
    return HttpResponse(request.POST)


def template(request):
    list1 = [0, 323, 45, 123, 34, 53423, 54, 23]
    context = {
        'test': 'TEXT',
        "list1": list1,
        "name": "Alex",
        "surname": "Jeson",
        "coords": {
            "x": '4',
            "y": "u coords",
        },
    }
    return render(request, 'aboutMe/template.html', context)