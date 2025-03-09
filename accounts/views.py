from django.contrib.auth.views import LoginView, PasswordChangeView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from accounts.forms import SignUpForm


# Create your views here.
class CustomLoginView(LoginView):
    template_name = 'login.html'


class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'password_change.html'
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    template_name = 'signup_form.html'
    form_class = SignUpForm
    success_url = reverse_lazy('login')
