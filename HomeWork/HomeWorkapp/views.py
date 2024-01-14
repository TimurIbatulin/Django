from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    with open("./about_me.html") as file:
        int_number = file.read()
    return HttpResponse(int_number)
# Create your views here.
