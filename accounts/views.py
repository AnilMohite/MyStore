from django.shortcuts import render, HttpResponse
from .forms import RegistrationForm
from .models import Account

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        print(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            user = Account.objects.create_user(
                first_name = first_name,
                last_name = last_name,
                email = email,
                password = password
            )
            user.phone_number = phone_number
            user.save()
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    return HttpResponse('login')