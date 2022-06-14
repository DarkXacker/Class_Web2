from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import *
from django.urls import reverse_lazy

# Create your views here.

class PupilListView(ListView):
    model = Pupil
    template_name = 'pupils/pupil_list.html'

class PupilDetailView(DetailView):
    model = Pupil
    template_name = 'pupils/pupil_detail.html'

class PupilCreateView(CreateView):
    model = Pupil
    template_name = 'pupils/pupil_create.html'
    fields = ('ism', 'familya', 'sharif', 'tug_kun', 'telefon', 'haqida', 'rasmi', )
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    # user superuser ekanini tekshirish
    
    def test_func(self):
        return self.request.user.is_superuser

class PupilEditView(UpdateView):
    model = Pupil
    template_name = 'pupils/pupil_edit.html'
    fields = ('ism', 'familya', 'sharif', 'tug_kun', 'telefon', 'haqida', 'rasmi', )

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user

class PupilDeleteView(DeleteView):
    model = Pupil
    template_name = 'pupils/pupil_delete.html'
    success_url = reverse_lazy('pupil_list')

    def test_func(self):
        obj = self.get_object()
        return obj.author == self.request.user
