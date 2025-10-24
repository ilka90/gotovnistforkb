from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse('<h4> Testing main page</h4>')

def about(request):
    return HttpResponse('<h4> About main page</h4>')
