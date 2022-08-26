from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

# def home(request):
#     return HttpResponse('Hi')

def home(request):
    return render(request, 'fsApp/index.html')
