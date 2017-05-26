from django.shortcuts import render
from .models import Post


def list(request):
    p=Post.objects.all()
    context={
        "p1":p
    }
    return render(request,"listpage.html",context)

def detailpost(request,id):
    p1=Post.objects.get(id=id)
    context={
        "p1":p1,
    }
    return render(request,"deatailpost.html",context)
