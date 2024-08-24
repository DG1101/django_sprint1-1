from django.shortcuts import render
from django.http import HttpResponse, HttpRequest


def about(request: HttpRequest) -> HttpResponse:
    template = 'pages/about.html'
    return render(request, template)


def rules(request: HttpRequest) -> HttpResponse:
    template = 'pages/rules.html'
    return render(request, template)
