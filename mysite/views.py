from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    data = {'header': 'Homepage', "message": "message welcome"}
    return render(request, "article_item.html", data)


def about(request):
    header = "About us"
    staff = ['John', "Lorem", 'Anoter Lorem']
    director = {"name": "some_name", "img": "/director.jpg"}
    adress = ('20', 'some city', 'befor', 'e')
    data = {"header": header, "staff": staff, "director": director, "address": adress}
    return render(request, 'about.html', data)
