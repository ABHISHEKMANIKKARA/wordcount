from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def count(request):
    fulltext=request.GET['fulltext1']
    WL=fulltext.split()
    WD={}
    for word in WL:
        if word in WD:
            WD[word]=WD[word]+1
        else:
            WD[word]=1
    return render(request,'count.html',{'fulltxt':fulltext,'worddictionary':WD})
def about(request):
    return render(request,'about.html')