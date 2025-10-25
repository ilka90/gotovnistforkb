from django.shortcuts import render

def index(request):
    data = {
        'title': 'Головна сторінка',
        'values': ['Some', 'Hello', '12345'],
        'obj': {
            'car': 'BMW',
            'age': 18,
            'hobby': 'football'      
        }
    }
    return render(request, 'main_page/index.html', data)

def about(request):
    return render(request, 'main_page/about.html')
