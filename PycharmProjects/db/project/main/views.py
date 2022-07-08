from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.shortcuts import render, get_object_or_404
# Create your views here.
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView

# from project.main.forms import RegisterUserForm
from .forms import *
from .models import *
from .utils import DataMixin


#from .. import projectapp
#from project.projectapp import *
#from project.projectapp import models
#from ..projectapp.models import Movie
from projectapp.models import Movie


class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/authorize.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))

class LoginUser(DataMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Register")
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('today')

def today(request):
    mov = Movie.objects.all()
    return render(request, 'main/today.html', {'mov': mov})

class NewsDetailView(DetailView):
    model = Movie
    template_name = 'main/info.html'
    context_object_name = 'movies'

