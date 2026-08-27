from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse("Hello, welcome to StudyBud!")
def about(request):
    a = 10 + 50
    return HttpResponse(f"About StudyBud! The answer is {a}")