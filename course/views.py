from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage1(request):
    return render(request, 'shop/homepage1.html')
