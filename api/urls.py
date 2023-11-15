from django.urls import path
from . import views

urlpatterns = [
    path('studentapi/',views.hello_world, name = 'studentapi'),
]