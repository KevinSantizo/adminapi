from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the peticiones index.")


from django.shortcuts import render

# Create your views here.
