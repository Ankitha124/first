from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def srujana(request):
    return HttpResponse('<marquee><h1>hai how are you</h1></marquee>')

def revi(request):
    return HttpResponse('<h1><b>mama kutti long drive polaamaa</b></h1>')

