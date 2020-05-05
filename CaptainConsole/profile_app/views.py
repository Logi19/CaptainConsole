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
    template_name = "profile_app/create_profile.html"

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')

        return render(request, self.template_name, {'form': form})

