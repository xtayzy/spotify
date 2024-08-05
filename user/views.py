from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST


from user.forms import SignUpForm, SignInForm
# Create your views here.


def signup(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')

    ctx = {
        'form': form
    }
    return render(request, 'user/signUp.html', ctx)


def signin(request):
    if request.user.is_authenticated:
        return redirect('index')
    form = SignInForm()
    if request.method == 'POST':
        form = SignInForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('index')
    ctx = {
        'form': form
    }
    return render(request, 'user/signIn.html', ctx)


def check_user_permission(request):
    return request.user.is_superuser


def logout_view(request):
    logout(request)
    return redirect('sign-in')
