from django.shortcuts import render
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
    form_class = ProfileForm

    # hvað gerir þetta fall?
    def register_profile_page(self, request):
        form = UserCreationForm
        return render(request=request,
                      template_name= "profile_app/create_profile.html, ", context={"form":form})

