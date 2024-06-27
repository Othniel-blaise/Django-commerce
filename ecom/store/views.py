from django.shortcuts import render,redirect
from .models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .forms import SignUpForm 
from django import forms 






def category(request, foo):
    # Replace hyphens with spaces
    foo = foo.replace('_', ' ')
    # Grab the category from the url
    try:
        #look up the category
        category = Category.objects.get(name=foo)
        products = Product.objects.filter(category=category)
        return render(request, 'category.html', {'products': products, 'category': category})
    except Category.DoesNotExist:
        messages.success(request, "The category does not exist.")
        return redirect('home')
    # except Exception as e:
    #     messages.error(request, f"An error occurred: {e}")
    #     return redirect('home')

def product(request,pk):
    product = Product.objects.get(id=pk)
    return render(request,'product.html', {'product': product})



def home(request):
    products = Product.objects.all()
    return render(request,'home.html', {'products': products})  

def about(request):
    return render(request,'about.html',{}) 

def login_user(request):

    if request.method == 'POST':
        username = request.POST['username'] 
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request,("You have been logged in..."))
            return redirect('home')
        else:
            messages.success(request,("There was an error, please try again"))
            return redirect('login')


    else:

        return render(request,'login.html',{}) 

def logout_user(request):
    logout(request)
    messages.success(request,("You have been logged out ... Thanks for stopping by ..."))
    return redirect('home')

def register_user(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            # Authentifier et connecter l'utilisateur
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "You have been registered...")
                return redirect('login')
            else:
                messages.error(request, "Authentication failed. Please try again.")
                return redirect('register')
        else:
            messages.error(request, "Whoops! There was an error, please try again.")
            return render(request, 'register.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})