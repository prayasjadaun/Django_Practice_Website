from django.shortcuts import render,HttpResponse
# Create your views here.
def home(request):
    return render(request,'home.html')
def business(request):
    return render(request,'business.html')
def politics(request):
    return render(request,'politics.html')
def tech(request):
    return render(request,'tech.html')
def about(request):
    return render(request,'about.html')

