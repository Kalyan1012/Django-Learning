from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, from blog!")

# Create your views here.
def about(request):
    return HttpResponse("Hello, from blog about!")
