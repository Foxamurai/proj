from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainAPIView.as_view(), name='home'),
    path('text', views.TextAPIView.as_view(), name='text'),
    path('file', views.FileAPIView.as_view(), name='file'),
    path('audio', views.AudioAPIView.as_view(), name='audio'),
]
