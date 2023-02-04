from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    lst = list(range(6, 15))
    return render(request, 'generator/home.html', {'lst': lst})


def password(request):

    char = [chr(i) for i in range(97, 123)]
    charupper = [chr(i) for i in range(65, 91)]
    charnumbr = [chr(i) for i in range(48, 58)]
    charspec = [chr(i) for i in range(33, 48)]+[chr(i) for i in range(58, 65)]+[chr(i) for i in range(91, 97)]+[chr(i) for i in range(123, 127)]

    length = int(request.GET.get('length'))
    upper = bool(request.GET.get('uppercase'))
    numbr = bool(request.GET.get('numbers'))
    spec = bool(request.GET.get('special'))

    psw = ''
    for i in range(length):
        if upper == True:
            if numbr == True:
                if spec == True:
                    psw += random.choice((char+charupper+charnumbr+charspec))
                else:
                    psw += random.choice((char + charupper + charnumbr))
            elif spec == True:
                psw += random.choice((char + charupper + charspec))
            else:
                psw += random.choice((char + charupper))
        elif numbr == True:
            if spec == True:
                psw += random.choice((char + charnumbr + charspec))
            else:
                psw += random.choice((char + charnumbr))
        elif spec == True:
            psw += random.choice((char + charspec))
        else:
            psw += random.choice(char)
    return render(request, 'generator/password.html', {'password': psw})
