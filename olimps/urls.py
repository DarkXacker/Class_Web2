from django.urls import path
from .views import *

urlpatterns = [
    path('', OlimpListView.as_view(), name='olimp_list'),
    path('olimp/<int:pk>/', OlimpDetailView.as_view(), name='olimp_detail'),
    path('create/', OlimpCreateView.as_view(), name='olimp_create'),
    path('edit/<int:pk>/', OlimpEditView.as_view(), name='olimp_edit'),
    path('delete/<int:pk>/', OlimpDeleteView.as_view(), name='olimp_delete'),
]