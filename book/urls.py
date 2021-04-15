from django.urls import path, re_path
from . import views


app_name = 'book'

urlpatterns = [

    # /book/{id}/
    path('<slug:pk>/', views.DetailView.as_view(), name='detail'),

    # /book/
    path('', views.IndexView.as_view(), name='book_list'),

]