from django.urls import path
from .views import *

urlpatterns = [
    path('', PupilListView.as_view(), name='pupil_list'),
    path('pupil/<int:pk>/', PupilDetailView.as_view(), name='pupil_detail'),
    path('create/', PupilCreateView.as_view(), name='pupil_create'),
    path('edit/pupil/<int:pk>/', PupilEditView.as_view(), name='pupil_edit'),
    path('delete/pupil/<int:pk>/', PupilDeleteView.as_view(), name='pupil_delete'),
]