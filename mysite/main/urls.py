from django.urls import path
from . import views

urlpatterns = [
    path('', views.MainApiView.as_view(), name='home'),
    path('text', views.FileApiView.as_view(), name='text'),

]
