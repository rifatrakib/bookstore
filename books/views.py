from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse('This is books index')


def book(request, id):
    return render(request, 'template', {'context': id})


def author(request, id):
    return render(request, 'template', {'context': id})
