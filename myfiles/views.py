from django.shortcuts import render
from myfiles.models import *
# Create your views here.
# read more, read less, FiU,

def about(a):
    return render(a,'about.html')

def contact(c):
    return render(c,'contact.html')

def design(d):
    return render(d,'design.html')

def index(i):
    return render(i,'index.html')

def shop(s):
    return render(s,'shop.html')