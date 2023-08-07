from django.shortcuts import render,redirect,reverse
# from typing import Protocol
# from django.template.loader import render_to_string
# from django.contrib.sites.shortcuts import get_current_site
# from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
# from django.utils.encoding import force_bytes,force_str
# from django.core.mail import EmailMessage
# from django.core.exceptions import ValidationError
# from django.core.validators import validate_email
# from django.db.models import Q
# from django.db.models.query_utils import Q
from django.http import HttpResponse,request
from myfiles.models import *
from django.contrib.auth.forms import UserCreationForm
from myfiles.forms import UserCreateForm,Subscribe_Newsletter_Form,Mail_Message_Form
from django.forms import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout,get_user_model
from django.contrib.auth.decorators import login_required
# Create your views here.
# read more, read less, FiU,

def sign_up(r):
    if r.user.is_authenticated:
        return redirect('index')
    else:
        form = UserCreateForm()
        if r.method == 'POST':
            form = UserCreateForm(r.POST)
            print('post')
            if form.is_valid():
                print('is_valid')
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(r, 'Account was created for' + user)
                return redirect('sign_in')
            else:
                return redirect('sign_up')
    return render(r,'sign_up.html',{'form1':form})

def sign_in(r):
    if r.user.is_authenticated:
        return redirect('index')
    else:
        if r.method == 'POST':
            username = r.POST.get('username')
            password = r.POST.get('password')
            user = authenticate(r,username=username,password=password)
            if user is not None:
                login(r,user)
                return redirect('index')
            else:
                messages.info(r,'Username OR Password is incorrect')
    return render(r,'sign_in.html')

def user_logout(r):
    logout(r)
    return redirect('sign_in')

@login_required(login_url='sign_in')
def about(a):
    return render(a,'about.html')

@login_required(login_url='sign_in')
def contact(c):
    return render(c,'contact.html')

@login_required(login_url='sign_in')
def design(d):
    return render(d,'design.html')

@login_required(login_url='sign_in')
def index(i):
    return render(i,'index.html')

@login_required(login_url='sign_in')
def shop(sh):
    form = Subscribe_Newsletter_Form()
    form2 = Mail_Message_Form()
    if 'Mail Message' in sh.POST:
        form2 = Mail_Message_Form(sh.POST)
        if form2.is_valid():
            form2.save()
            messages.success(sh, 'Message has been send to the Mail List.')
            "Xabar pochta ro'yxatiga yuborildi."
            return redirect('shop')
        else:
            messages.error(sh, 'Message hasn\'t been send to the Mail List.')
            "Xabar pochta ro'yxatiga yuborilmadi."
            return redirect('shop')
    elif sh.method == 'POST':
        form = Subscribe_Newsletter_Form(sh.POST)
        if form.is_valid():
            form.save()
            messages.success(sh, 'Subscription Successful.')
            'obuna muvaffaqiyatli.'
            return redirect('shop')
        else:
            messages.error(sh, 'Subscription failed, Email is invalid.')
            'Obuna amalga oshmadi, elektron pochta manzili yaroqsiz.'
            return redirect('shop')
    return render(sh,'shop.html',{'form':form,'form2':form2})