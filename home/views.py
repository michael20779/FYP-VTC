from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.
def HomeView(request):
    return render(request, 'index.html')

def LoginView(request):
    return render(request, 'login.html')

def HistoryView(request):
    return render(request, 'history.html')

def SignupView(request):
    return render(request, 'signup.html')

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