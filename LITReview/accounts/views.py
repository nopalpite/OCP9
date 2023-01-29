from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def signup(request):
    if request.method != 'POST':
        form = UserCreationForm()
    else:
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:signin')

    context = {'form': form}
    return render(request, 'accounts/signup.html', context)

def signin(request):
    if request.method != 'POST':
        form = AuthenticationForm(request)
    else:
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/reviews/feeds/')

    context = {'form': form}
    return render(request, 'accounts/signin.html', context)

@login_required
def signout(request):
    logout(request)
    return redirect('/accounts/signin/')

