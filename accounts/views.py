from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm

def register(request):
    form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    return HttpResponse('login')