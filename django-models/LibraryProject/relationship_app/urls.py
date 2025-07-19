from django.urls import path
from .views import RegisterView, LoginView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('register/', RegisterView.as_view(template_name='relationship_app/register.html'), name='register'),
    path('register/', views.register, name='register'),
    path('login/', LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name='librarian_view'),
    path('member-page/', views.member_view, name='member_view'),
]
