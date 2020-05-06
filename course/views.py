from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homepage(request):
    return render(request, 'shop/homepage.html')
