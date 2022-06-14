from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .forms import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

@login_required
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, request.FILES, instance=request.user)

        if user_form.is_valid():
            user_form.save()
            messages.success(request, 'Your profile is updated successfully')
            return redirect(to='home')
    else:
        user_form = UpdateUserForm(instance=request.user)

    return render(request, 'registration/settings.html', {'user_form': user_form})
