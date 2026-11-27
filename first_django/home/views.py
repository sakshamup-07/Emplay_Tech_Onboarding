from operator import index

from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
def delta(request):
    data = {
        'name' : 'Saksham Upadhyay',
        'age' : 20,
        'city' : 'Lucknow'
    }
    return render(request , 'index.html' , context=data)
def services(request):
    return HttpResponse("This is the services page of my first Django project.")