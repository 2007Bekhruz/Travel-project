from django.urls import path
from . import views

urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/registration/', views.registration_view, name='registration'),
    path('accounts/logout/', views.logout_view, name='logout'),
]