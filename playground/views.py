from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def sayHello(request):
    return render(request,'index.html',{'name':'ritvik'})

def fact(request):
    num = int(request.GET['number'])
    res = fact2(num)
    return render(request,'result.html',{'value':res})

def fact2(number):
    if(number <= 1):
        return 1
    return number*fact2(number-1)