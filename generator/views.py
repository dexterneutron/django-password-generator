from django.shortcuts import render
from django.http import HttpResponse

import random
# Create your views here.
def home(request):
    return render(request, 'generator/home.html')

def password(request):
    char_list=list('abcdefghijklmnopqrstuvwxyz')

    if request.GET.get('uppercase'):
        char_list.extend('ABCDEFGHIJK')

    if request.GET.get('special'):
        char_list.extend('''!#$%&'()*+,-./:;<=>?@[\]^_`{|}~''')

    if request.GET.get('number'):
        char_list.extend('1234567890')

    length = int(request.GET.get('length', 12))
    generated_password=''

    for _ in range (length):
        generated_password += random.choice(char_list)
    
    return render(request, 'generator/password.html', {'password':generated_password})

def about(request):
    return render(request, 'generator/about.html')