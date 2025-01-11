from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        pno = request.POST.get('pno')
        email = request.POST.get('email')
        add = request.POST.get('address')
        un = request.POST.get('un')  
        pw = request.POST.get('pw')
        DO = Data(name=name, pno=pno, email=email, add=add, username=un, password=pw)
        DO.save()
        return HttpResponse('Registration Successfull')
    return render(request, 'register.html')