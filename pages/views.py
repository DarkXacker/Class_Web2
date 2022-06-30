from django.views.generic import TemplateView
from django.shortcuts import render

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'home.html'

def error_404(request, exception):
    return render(request, 'errors/404.html')