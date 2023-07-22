from django.shortcuts import render,redirect,reverse

from django.http import HttpResponse,request
from django.forms import inlineformset_factory
from myfiles.models import *
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from myfiles.forms import UserCreateFormShop,CommentForm
from django.db.models import Q
from django.forms import *
from django.contrib.auth.models import User

from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# Create your views here.
