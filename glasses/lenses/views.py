from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'index.html',{})
def about(request):
    return render(request,'about.html',{}) #{} would hold variables
def contact(request):
    return render(request,'contact.html',{}) # 

def products(request):
    return render(request,'products.html',{}) # query the products and return them to the interface

def distributor(request):
    return render(request,'distributor.html',{})