from django.contrib import admin
from .models import Category, Course, Module, Lesson


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'icon', 'created_at', 'updated_at')
    search_fields = ('name', 'description', 'icon')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'teacher', 'category', 'price', 'discount_price', 'is_published', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'category', 'price', 'discount_price')

@admin.register(Module)
class ModuleAdmin(admin.ModelAdmin):
    list_display = ('id', 'course', 'title', 'order', 'created_at', 'updated_at')
    search_fields = ('title', 'description', 'course', 'order')

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('id', 'module', 'title', 'video_url', 'duration', 'order')
    search_fields = ('module', 'title', 'content', 'video_url', 'order')