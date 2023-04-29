from django.shortcuts import render

# Create your views here.



def usd(request):
    d={'d':'ENGINEERING','r':'hloo hii iam groot'}


    return render(request,'usdfilters.html',d)