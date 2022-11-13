from django.shortcuts import render
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib import login, logout

