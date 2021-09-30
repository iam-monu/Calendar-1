from django.shortcuts import render
from .models import *

# Create your views here.
def home(request):
    events= Events.objects.all()
    # customers=Customer.objects.all()
    # context ={'events':events ,'customers':customers}
    return render(request,'users/home.html',{'events':events ,})

def login_views(request):
    return render(request,'users/login.html')


def register_views(request):
    return render(request,'users/register.html')

def customer_event(request):
    events = Events.objects.all()
    customers=Customer.objects.all()
    context ={'events':events ,'customers':customers}
    return render(request, 'users/customerevent.html',context)