from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1>this is first</h1>')
def second(request):
    return HttpResponse('<h1>this is seconds</h1>')
