from django.urls import path, re_path
from . import views

# /account/
app_name = 'account'

urlpatterns = [
    # /account/register/
    path('register/', views.register, name='register'),

    # /account/login.
    path('login/', views.login_user, name='login_user'),

    # /account/logout_user/
    path('logout_user/', views.logout_user, name='logout_user'),
]