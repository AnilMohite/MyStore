from django.shortcuts import render, HttpResponse

def register(request):
    return HttpResponse('register')

def login(request):
    return HttpResponse('login')