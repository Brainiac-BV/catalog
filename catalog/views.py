from django.shortcuts import render
from django.shortcuts import HttpResponse
# Create your views here.

def home_view(request):
    if request.user.is_authenticated:
        return render(request, 'base_generic.html')
    else:
        return HttpResponse("this guy is trash")


def catalog_view(request):
    return render(request, 'catalog.html')
    #return HttpResponse("catalogs go here...")


def books_view(request):
    return render(request, 'books.html')