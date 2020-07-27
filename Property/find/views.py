from django.shortcuts import render, redirect
from .models import *
from .forms import *
from datetime import datetime
from django.contrib.auth.decorators import login_required
from registration.models import *

@login_required(login_url = '/login')
# def display(request):
#     addresses = Address.objects.all()
#     homes = Home.objects.all()
#     context = {
#         'addresses': addresses,
#         'homes': homes
#         }

#     return render(request, 'find/display.html', context)

@login_required(login_url = '/login')
def dashboard(request):
    addresses = Address.objects.filter(agent = request.user)
    context = {
        'addresses': addresses,
    }
    return render(request, 'find/agent-dashboard.html', context)


@login_required(login_url = '/login')
def my_listings(request):
    addresses = Address.objects.filter(agent = request.user)
    homes = Home.objects.all()
    context = {
        'addresses': addresses,
        'homes': homes
        }

    return render(request, 'find/my-listings.html', context) 

@login_required(login_url = '/login')
def create_listing(request):
    address_form = AddressForm()
    home_form = HomeForm()
    if request.method == 'POST':
        address_form = AddressForm(request.POST)
        home_form = HomeForm(request.POST, request.FILES)
        if all([address_form.is_valid(), home_form.is_valid()]):
            address = address_form.save(commit=False)
            home = home_form.save(commit=False)
            address.agent = request.user
            address.save()
            home.address = address
            home.save()
    
            return redirect('/agents/')
        else:
            address_form.errors
            home_form.errors


    context = {
        'address_form': address_form,
        'home_form': home_form,

        }
    return render(request, 'find/create-listing.html', context)

@login_required(login_url = '/login')
def update_listing(request, pk):
    address = Address.objects.get(id=pk)
    home = Home.objects.get(address = address.id)
    address_form = AddressForm(instance=address)
    home_form = HomeForm(instance=home)
    if request.method == 'POST':
        address_form = AddressForm(request.POST, instance=address)
        home_form = HomeForm(request.POST, request.FILES, instance=home)
        if all([address_form.is_valid(), home_form.is_valid()]):
            address = address_form.save(commit=False)
            home = home_form.save(commit=False)
            address.agent = request.user
            address.save()
            home.address = address
            home.save()
    
            return redirect('/agents/')
        else:
            address_form.errors
            home_form.errors


    context = {
        'address_form': address_form,
        'home_form': home_form,

        }
    return render(request, 'find/create-listing.html', context)
    

@login_required(login_url = '/login')
def view_listing(request, pk):
    address = Address.objects.get(id=pk)
    home = Home.objects.get(address=address.id)
    agent = address.agent
    context = {
        'address': address,
        'home': home,
        'agent': agent
    }

    return render(request, 'find/view.html', context)



@login_required(login_url = '/login')
def delete_listing(request,pk):
    listing = Address.objects.get(id=pk)
    if request.method == 'POST':
        listing.delete()
        return redirect('/agents/')
    