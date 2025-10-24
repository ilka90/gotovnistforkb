from django.shortcuts import render

def index(request):
    return render(request, 'main_page/index.html')

def about(request):
    return render(request, 'main_page/about.html')
