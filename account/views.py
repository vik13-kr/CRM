from django.shortcuts import render, redirect

from .models import *
from .forms import *
from django.contrib.auth import authenticate, login as dj_login , logout as dj_logout

from django.contrib.auth.decorators import login_required

from django.contrib import messages
from .decorators import unauthenticated_user

@unauthenticated_user
def register(request):
    form = UserRegisterForm()
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'account/register.html', context)

@unauthenticated_user
def login(request):
    form  = UserLogin()
    
    if request.method == "POST":
        form = UserLogin(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
       

            user = authenticate(request,username = username, password = password)

            if user is not None :
                dj_login(request,user)
                return redirect('/')
            else:
                messages.info(request, 'Username or Password is incorrent')


    context = {'form': form}
    return render(request, 'account/login.html', context)

def logout(request):
    dj_logout(request)
    return redirect('login')

#view for homepage
@login_required(login_url = 'login')
def homepage(request):
    customers = Customer.objects.all()
    #orders = Order.objects.all()
    #order by latest
    orders = Order.objects.order_by('-date_ordered')

    orders_count = Order.objects.all().count()
    orders_delivered = Order.objects.filter(status = "Delivered").count()
    orders_pending = Order.objects.filter(status = "Pending").count()

    context = {'customers': customers,
                 'orders': orders,
                 "orders_count":orders_count,
                 'orders_delivered':orders_delivered ,
                 'orders_pending': orders_pending }

    return render(request,'account/dashboard.html',context)

@login_required(login_url = 'login')
def product(request):
    products = Product.objects.all()
    return render(request,'account/product.html',{'products': products})

@login_required(login_url = 'login')
def customer(request, pk):    
    customer_details = Customer.objects.get(pk = pk)  

    orders_count = Order.objects.filter(customer__pk=pk).count() #reverse query
    orders= Order.objects.filter(customer__pk=pk)

    context = {
        'customer_details' : customer_details,
        'orders_count' : orders_count,
        'orders' : orders
    }
    return render(request,'account/customer.html', context )

@login_required(login_url = 'login')
def create_order(request):

    form = CreateOrderForm()
    if request.method == 'POST':
        form = CreateOrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request,'account/create_order.html', context )

@login_required(login_url = 'login')
def update_order(request, pk):

    instance = Order.objects.get(pk = pk)
    form = CreateOrderForm(instance=instance) #passing all the information associated with the order instance in the form.

    if request.method == 'POST':
        form = CreateOrderForm(request.POST, instance=instance)
        if form.is_valid():
            form.save()
            return redirect('dashboard')

    context = {'form': form}
    return render(request,'account/update_form.html',context )

@login_required(login_url = 'login')
def delete_order(request, pk):

    instance = Order.objects.get(pk = pk)

    if request.method == 'POST':
        instance.delete()
        return redirect('dashboard')
    

    context = {'instance': instance}
    return render(request,'account/delete_order.html', context )

