from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView

from .models import Profile


class ProfileDetail(DetailView):
    model = Profile

class ProfileUpdate(UpdateView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile

    def operation(self):
        # TODO: implement function
        pass

