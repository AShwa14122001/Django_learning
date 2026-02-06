"""
URL configuration for project2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('accounts.urls')),
]

urlpatterns += [
    path('login/', auth_view.LoginView.as_view(template_name='login.html'), name='login'),
    path('user_dashboard', auth_view.LoginView.as_view(template_name="user_dashboard.html"), name = "user_dashboard"),
    path('manager_dashboard', auth_view.LoginView.as_view(template_name="manager_dashboard.html"), name = "manager_dashboard"),
    path('admin_dashboard', auth_view.LoginView.as_view(template_name="admin_dashboard.html"), name = "admin_dashboard"),
    path('logout/',auth_view.LogoutView.as_view(), name="logout"),
]