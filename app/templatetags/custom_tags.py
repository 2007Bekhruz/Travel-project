from django import template
from app.models import Category, Services, Products

register = template.Library()

@register.simple_tag()
def get_categories():
    categories = Category.objects.all()
    return categories


@register.simple_tag()
def get_services():
    services = Services.objects.all()
    return services


@register.simple_tag()
def get_products():
    products = Products.objects.all()
    return products