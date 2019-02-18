from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        return HttpResponse("<h1>Test</h1>")
    else:
        return HttpResponse("this guy is trash")


def catalog_view(request):
    return HttpResponse("catalogs go here...")