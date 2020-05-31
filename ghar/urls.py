from . import views
from django.urls import path

urlpatterns = [
    path('',views.myghar,name='myghar'),
    path('contact/',views.contact,name='contact'),
]