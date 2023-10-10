from django.shortcuts import render
from django.http import HttpResponse

def m1(request):
    return render(request,template_name='opp.html')
def caal(request):
    i=request.POST["t1"]
    j=request.POST["t2"]
    op=request.POST["operation"]
    x=int(i)
    y=int(j)
    z=0
    if op=="mul":
        z=x*y
    elif op=="add":
        z=x+y
    elif op=="sub":
        z=x-y
    else :
        z=x/y
    con_dic={'rec':z}
    return render(request,template_name='result.html',context=con_dic)


# Create your views here.
