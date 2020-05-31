from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact
from django.contrib import messages

def myghar(request):
    return render(request,'ghar/index.html')

def contact(request):
  if request.method=="POST":
    name=request.POST.get('name','')
    email=request.POST.get('email','')
    message=request.POST.get('message','')
    contact = Contact(name=name,email=email,message=message)
    contact.save()
    messages.success(request, f' Hi {name}! We received your message and will respond shortly!')

  return render(request, 'ghar/index.html')