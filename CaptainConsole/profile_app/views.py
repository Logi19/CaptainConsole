from django.shortcuts import render

# Create your views here.

class ProfileUpdate(UpdateView):
    model = Profile

class ProfileDetail(DetailView):
    model = Profile

class ProfileCreate(CreateView):
    model = Profile

    def operation(self):
        pass

