from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def three(request):
    return HttpResponse('<marquee><h1>free-bird</marquee></h1>')
def four(request):
    return HttpResponse('<marquee><h1> CHARAN IS GOOD</marquee></h1>')

