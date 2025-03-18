# Connect4Master/urls.py
from django.contrib import admin
from django.urls import path, include
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.login_view, name='home'),  # Root URL redirects to login view
    path('', views.register_view, name='register_view'),
    path('login/', views.login_view, name='login_view'),
    path('index/', views.index_view, name='index_view'),
    path('playwithfriend/', views.playwithfriend_view, name='playwithfriend'),
    path('playwithcomputer/', views.playwithcomputer_view, name='playwithcomputer'),
    

]
