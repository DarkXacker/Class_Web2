from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .forms import *

from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import send_mail
from django.conf import settings

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    
    def index(request):
        import random
        a = random.random()
        num = str(a)
        token = num.split('.')[1]

        domain_name = get_current_site(request).domain
        link = f"http://{domain_name}/verify/{token}"
        send_mail(
            "Email Tasdiqlash", f"Email Manzilni tasdiqlash uchun {link} ni ustiga bosing", settings.EMAIL_HOST_USER, [email], fail_silently=False)

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