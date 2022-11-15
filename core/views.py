from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages,auth
from.models import *

# Create your views here.
def sign_up(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST ['email']
        firstname = request.POST ['firstname']
        lastname = request.POST ['lastname']
        passwword = request.POST ['password']
        password2 = request.POST ['password2']

        if passwword == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'Username already taken!')
                return redirect('signup')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'email already taken!')
                return redirect('signup')
            else:
                new_user = User.objects.create_user(username=username, email=email,  password=passwword)
                new_user.is_active = False
                new_user.first_name = firstname
                new_user.last_name = lastname
                new_user.save()

                user_model = User.objects.get(username=username)
                user_profile = Authentication.objects.create(user=user_model, id_user = user_model.id) 
                return redirect('login')
        
        else:
            messages.info(request, 'Password Not Matching')
            return redirect ('signup')
            
    else:
        return render(request, 'signup.html')
    
def home (request):
    return render (request, 'home.html')

def login (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST ['password']

        

        user = auth.authenticate(username =username, password =password)

        if user is not None:
            auth.login( request, user)
            return redirect('/')
        else:
            messages.info(request, 'credentials Invalid')
            return redirect ('login')
     


    else:
        return render(request, 'login.html')
   