from django.urls import path
from .views import *
urlpatterns = [
    path('', home_view, name='home'),
    path('categories/', categories_view, name='categories')
]