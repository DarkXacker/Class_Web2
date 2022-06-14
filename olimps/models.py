from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField

from django.utils import timezone

# Create your models here.

class Olimp(models.Model):
    nomi = models.CharField(max_length=100)
    sharti = RichTextField()
    rasmi = models.ImageField(upload_to='olimps/', blank=True)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(get_user_model(), on_delete = models.CASCADE)
        
    name = models.CharField(max_length=500, blank=True)
    videofile= models.FileField(upload_to='videos/', null=True, verbose_name="", blank=True)

    def __str__(self):
        return self.name + ": " + str(self.videofile)
    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.nomi

    def get_absolute_url(self):
        return reverse('olimp_detail', args=[str(self.id)])

class BlogComment(models.Model):
    blogpost_connected = models.ForeignKey(
        Olimp, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.blogpost_connected} - {self.author}"