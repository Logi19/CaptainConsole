
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.messages import get_messages

from store_app.models import Order, OrderItem
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
            print(f"Failed login attempt with email: {email}")
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'registration/login.html')


@login_required
def logout_view(request, *args, **kwargs):
    logout(request)
    return HttpResponseRedirect('/store/')


@login_required
def my_profile_view(request, *args, **kwargs):
    context = {'user': request.user}
    order_list = list(Order.objects.filter(profile_id=request.user.id))
    order_list.sort(key=lambda x: x.date, reverse=True)
    order_item_list = []
    for order in order_list:
        order_item_list.append((order, list(OrderItem.objects.filter(order=order.id))))
    context['order_history'] = order_item_list
    return render(request, 'profile_app/view_profile.html', context)


@login_required
def my_profile_update(request, *args, **kwargs):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            new_first_name = request.POST.get('first_name')
            new_last_name = request.POST.get('last_name')
            if 'profileImage' in request.FILES:
                new_profile_image = request.FILES['profileImage']
            else:
                new_profile_image = None

            profile = Profile.objects.get(id=request.user.id)

            profile.first_name = new_first_name
            profile.last_name = new_last_name
            if new_profile_image is not None:
                profile.profileImage = new_profile_image

            profile.save()
            messages.success(request, 'Profile successfully updated!')
            return HttpResponseRedirect('')
    else:
        data = {'first_name': request.user.first_name, 'last_name': request.user.last_name}
        form = ProfileForm(initial=data)
        context = {'user': request.user, 'form': form, 'messages': get_messages(request)}
        return render(request, 'profile_app/edit_profile.html', context)



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


