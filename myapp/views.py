from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from myapp.models import Product
from myapp.forms import ProductForm
from django.http import HttpResponse

def index(request):
    return HttpResponse("<h1>Hello, World</h1>")

def home(request):
    product_list = Product.objects.all()
    return render(request,'home.html',{'user_list':user_list})

def add(request):
    product_list = Product.objects.all()
    form = ProductForm()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/home/')
    return render(request,'add.html',{'form':form})

def edit(request,pk):
    edit = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=edit)
        if form.is_valid():
            form.save()
            return redirect('/home/', pk=edit.pk)
    else:
        form = ProductForm(instance=edit)
    return render(request,'edit.html',{'form':form,'edit':edit})

def delete(request, pk):
    delt = get_object_or_404(User, pk=pk)
    delt_pk = delt.pk
    delt.delete()
    return redirect('/home/',pk=delt_pk)


