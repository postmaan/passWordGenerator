
from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def aboutus(request):
    return render(request,'generator/aboutus.html')

def password(request):
    charachters = list('abcdefghijklmnopqrstuvwxyz0987654321')


    if request.GET.get('uppercase'):
        charachters.extend(list('ABCDEFGHIJKLMNOPQSTUVWXYZ'))
    if request.GET.get('special'):
        charachters.extend(list('!@#$%^&*'))
    if request.GET.get('numbers'):
        charachters.extend(list('0987654321'))

    length = int(request.GET.get('length',12)) # ? Why????? and How
    thepassword =''
    for x in range(length):
        thepassword += random.choice(charachters)




    #thepassword = 'Em!r@t3sGr0up'
    return render(request,'generator/password.html',{'password':thepassword})
