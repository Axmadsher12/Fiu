from django.shortcuts import render
from myfiles.models import *
# Create your views here.
# read more, read less, FiU,
def sign_in(si):
    return render(si,'sign_in.html')

def sign_up(su):
    return render(su,'sign_up.html')

def about(a):
    return render(a,'about.html')

def contact(c):
    return render(c,'contact.html')

def design(d):
    return render(d,'design.html')

def index(i):
    return render(i,'index.html')

def shop(sh):
    return render(sh,'shop.html')