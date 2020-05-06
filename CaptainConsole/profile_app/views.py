
from django.http import HttpResponseRedirect
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

from .models import Profile
from .forms import ProfileForm

class ProfileDetail(DetailView):
    model = Profile

class ProfileUpdate(UpdateView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile
    form_class = UserCreationForm
    template_name = "profile_app/create_profile.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            """
            process form cleaned data
            Redirect to the login screen
            """
            return HttpResponseRedirect('/login/')

        return render(request, self.template_name, {'form': form})

