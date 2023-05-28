from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_display_link = ('pk', 'title')
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'slug')
    list_display_link = ('pk', 'title')
    prepopulated_fields = {"slug": ("title",)}


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'title', 'description', 'price', 'is_available', 'category', 'slug')
    list_display_links = ('pk', 'title')
    list_filter = ('services', 'category')
    prepopulated_fields = {'slug' : ('title',)}
    inlines = [ProductImageInline]
    list_editable = ('is_available', 'price')