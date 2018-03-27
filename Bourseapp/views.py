from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello():
    text ="<h1>welcome to my app number </h1>"
    return HttpResponse(text)

