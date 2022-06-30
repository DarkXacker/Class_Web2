from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

# Create your models here.

class Pupil(models.Model):
    ism = models.CharField(max_length=100)
    familya = models.CharField(max_length=100)
    sharif = models.CharField(max_length=100)
    tug_kun = models.DateField()
    telefon = models.IntegerField()
    haqida = RichTextField()
    rasmi = models.ImageField(upload_to='pupils/', blank=True)
    
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.ism

    def get_absolute_url(self):
        return reverse('pupil_detail', args=[str(self.id)])