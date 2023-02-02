from django.shortcuts import render
from django.views.generic import ListView
from django.shortcuts import  render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate 
from django.contrib.auth.forms import AuthenticationForm 


# Create your views here.
def HomeView(request):
    return render(request, 'index.html')
    
def LoginView(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def SignupView(request):
    if request.method == "POST":
            form = NewUserForm(request.POST)
            if form.is_valid():
                user = form.save()
                login(request, user)
                messages.success(request, "Registration successful." )
                return redirect("/")
            messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="signup.html", context={"register_form":form})

def HistoryView(request):
    return render(request, 'history.html')



def PriceView(request):
    return render(request, 'pricing.html')

def ProductView(request):
    return render(request, 'product.html')

def CompetitionView(request):
    return render(request, 'competition.html')

def CartView(request):
    return render(request, 'cart.html')

def CheckoutView(request):
    return render(request, 'checkout.html')

def PaymentView(request):
    return render(request, 'payment.html')

def PaymentSuccessView(request):
    return render(request, 'payment-success.html')