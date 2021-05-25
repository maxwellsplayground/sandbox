from django.shortcuts import render,redirect, HttpResponse
from . import forms
from .forms import CoffeeShopForm,CoffeeOptionForm, ProfileForm, UploadForm
from .tables import *
from tkinter import Tk
from tkinter.filedialog import askdirectory
from .models import CoffeeShop, CSVFile
import csv

# Create your views here.
def index(request):
    print("hello")
    form = ProfileForm

    if request.method == 'GET':
        print('get has begot')
        return render(request,'index.html',{'form':form})
    
    if request.method =='POST':
        data = request.POST.copy()
        
        print('post schmost')
        print(data)
   
        return render(request,'index.html',{})

def shopInfo(request, id):
    print(request,id)
    coffeeshop = CoffeeShop(id=id)
    print(coffeeshop.name)
    print(coffeeshop.id)
    print(coffeeshop)
    return render(request,'shops.html',{'shop':coffeeshop})