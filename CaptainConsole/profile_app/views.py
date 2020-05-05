from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from .models import Profile
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm


class ProfileDetail(DetailView):
    model = Profile

class ProfileUpdate(UpdateView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile

    def register_profile_page(self, request):
        form = UserCreationForm
        return render(request=request,
                      template_name= "profile_app/create_profile.html, ", context={"form":form})

