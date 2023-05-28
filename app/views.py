from django.shortcuts import render
from .models import *


# Create your views here.
def home_view(request):
    return render(request, 'pages/index.html')


def categories_view(request):
    categories = Category.objects.all()
    context = {
        "categories": categories
    }
    return render(request, 'pages/index.html', context)


