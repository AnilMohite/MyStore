from django.shortcuts import render, HttpResponse, redirect
from .forms import RegistrationForm
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required

#verification
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
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

            # send verification link
            try:
                current_site = get_current_site(request)
                email_subject = "Activate Your Account"
                email_message = render_to_string('accounts/accounts_verification_mail.html',{
                    'user':user,
                    'domain':current_site,
                    'uid':urlsafe_base64_encode(force_bytes(user.id)),
                    'token': default_token_generator.make_token(user)
                })
                to_email = email
                send_email = EmailMessage(email_subject, email_message, to=[to_email])
                send_email.send()
            except Exception as e:
                Warning(f"Error while sending email: {str(e)}" )
                messages.error(request, "Error while sending verification link on mail.")

            msg = f"Welcome to Mystore! 🚀 We've sent a verification link to {email}. Click it to activate your account. Cheers to new beginnings!"
            return redirect('/accounts/register/?msg='+msg)
    else:
        form = RegistrationForm()
    context = {
        'form':form
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        print(email, password)
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            print('ss')
            auth.login(request, user)
            messages.success(request, "Logged in successfully!")
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')
    return render(request, 'accounts/login.html')

@login_required(login_url="login")
def logout(request):
    auth.logout(request)
    messages.success(request, "Logged out successfully.")
    return redirect('home')


def activate(request, uidb64, token):
    return HttpResponse('Ok')