# Django Imports
from django.views.generic import TemplateView
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Project Imports
from .forms import AgentForm,CreateUserForm


def Register(request):
    user_form = CreateUserForm()
    agent_form = AgentForm()

    if request.method == "POST":
        user_form = CreateUserForm(request.POST)
        agent_form = AgentForm(request.POST, request.FILES)
        if all([user_form.is_valid(), agent_form.is_valid()]):
            user = user_form.save()
            agent = agent_form.save(commit=False)
            agent.user = user
            agent.save()    
            return redirect('/agents/')
        else:
            user_form.errors
            agent_form.errors


    context = {
        'user_form': user_form,
        'agent_form': agent_form
    }

    return render(request, 'registration/agent-register.html', context)


def LoginAgent(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/agents/')
        
        else:
            messages.info(request, 'Username OR password is inccorect')
            return render(request, 'registration/agent-login.html')



    return render(request, 'registration/agent-login.html')

@login_required(login_url = '/login')
def LogoutAgent(request):
    logout(request)

    return redirect('/login')
