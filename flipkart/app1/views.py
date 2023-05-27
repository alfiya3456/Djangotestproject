from django.http import HttpResponse
from django.shortcuts import render
from .models import Product

# Create your views here.


def index(request):
    return HttpResponse("Hai dears")

def test_fun(request):
    return render(request,'test.html')
