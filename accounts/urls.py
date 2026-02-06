from django.urls import path
from .views import role_redirect,admin_dashboard,manager_dashboard,user_dashboard

urlpatterns=[
    path('admin-dashboard/', admin_dashboard),
    path('manager-dashboard/', manager_dashboard),
    path('user-dashboard/',user_dashboard),
    path('redirect/',role_redirect)
]