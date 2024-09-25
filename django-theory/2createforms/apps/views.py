# views.py
from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request,"login.html")

def postuser(request):

    name = request.POST.get("name", "Undefined")
    age = request.POST.get("age", 1)
    return HttpResponse(f"<h2>Name: {name}  Age: {age}</h2>")