from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy
from .forms import NewCommentForm

# Create your views here.

class OlimpListView(ListView):
    model = Olimp
    template_name = 'olimps/olimp_list.html'

class OlimpDetailView(DetailView):
    model = Olimp
    template_name = 'olimps/olimp_detail.html'

    def showvideo(request):

        lastvideo = Olimp.objects.last()

        videofile = lastvideo.videofile
        
        context = {
            'videofile': videofile,
        }
        
        return render(request, 'olimps/olimp_detail.html', context)

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)

        comments_connected = BlogComment.objects.filter(
            blogpost_connected = self.get_object()).order_by('-date_posted')
        
        data['comments'] = comments_connected
        
        if self.request.user.is_authenticated:
            data['comment_form'] = NewCommentForm(instance = self.request.user)

        return data

    def post(self, request, *args, **kwargs):
        new_comment = BlogComment(content = request.POST.get('content'), 
            author = self.request.user, blogpost_connected = self.get_object()
        )
        new_comment.save()
        
        return self.get(self, request, *args, **kwargs)

class OlimpCreateView(CreateView):
    model = Olimp
    template_name = 'olimps/olimp_create.html'
    fields = ('nomi', 'sharti', 'rasmi', 'name', 'videofile')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    
    def test_func(self):
        return self.request.user.is_superuser

class OlimpEditView(UpdateView):
    model = Olimp
    template_name = 'olimps/olimp_edit.html'
    fields = ('nomi', 'sharti', 'rasmi', 'name', 'videofile')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class OlimpDeleteView(DeleteView):
    model = Olimp
    template_name = 'olimps/olimp_delete.html'
    success_url = reverse_lazy('olimp_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
