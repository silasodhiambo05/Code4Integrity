from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import EnigmaAdmin, USSD, Investigation, User, Mlmodel
# Create your views here.

def index(request):

    dests = EnigmaAdmin.objects.all()
    return render(request,'base.html',{'dests': dests})


def investigation(request):

    dests = Investigation.objects.all()
    return render(request,'investigations.html',{'dests': dests})



def ussd(request):

    dests = USSD.objects.all()
    return render(request,'reports-ussd.html',{'dests': dests})


def user(request):

    dests = User.objects.all()
    return render(request,'reports-user.html',{'dests': dests})


def mlmodel(request):

    dests = Mlmodel.objects.all()
    return render(request,'reports-ml.html',{'dests': dests})







