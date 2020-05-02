from django.shortcuts import render

#view for homepage
def homepage(request):
    return render(request,'account/dashboard.html')

def product(request):
    return render(request,'account/product.html')

