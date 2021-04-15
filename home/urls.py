from django.urls import path, re_path
from . import views


app_name = 'home'

urlpatterns = [
    # /home/
    path('', views.index, name='index'),
]