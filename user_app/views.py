from django.shortcuts import render, redirect
from .email_backend import EmailBackend
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib import login, logout
from django.urls import reverse



def account_register(request):
    userForm = CustomUserForm(request.POST or None)
    context = {
        'form1': userForm,
    }
    if request.method == 'POST':
        if userForm.is_valid():
            user = userForm.save(commit=False)
            user.save()
            messages.success(request, "Account created. You can login now!")
            return redirect(reverse('account_login'))
        else:
            messages.error(request, "Provided data failed validation")
            # return account_login(request)
    return render(request, "voting/registration.html", context)


