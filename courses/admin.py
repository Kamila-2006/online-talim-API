from django.contrib import admin
from .models import Category, Course, Module, Lesson


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'icon')