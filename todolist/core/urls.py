from django.urls import path
from . import views

urlpatterns = [
        path('signup', views.RegistView.as_view(), name='signup'),
        path('login', views.LoginView.as_view(), name='login')
]

