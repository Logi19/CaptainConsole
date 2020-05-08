
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

from .models import Profile
from .forms import ProfileForm
from .forms import SignUpForm


def login_view(request, *args, **kwargs):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect('/store/')
            else:
                return HttpResponse("Your account is inactive.")
        else:
            print(f"Failed login attempt with email: {email} and password: {password}")
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html')


@login_required
def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/store/')



class ProfileDetail(DetailView):
    model = Profile


class ProfileUpdate(UpdateView):
    model = Profile


def sign_up_view(request, *args, **kwargs):
    if request.method == 'POST':

        form = SignUpForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(email=email, password=raw_password)
            login(request, user)
            return HttpResponseRedirect('/store/')

    else:
        form = SignUpForm()
    return render(request, 'registration/sign_up.html', {'form': form})


