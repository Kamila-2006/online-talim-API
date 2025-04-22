from rest_framework import serializers
from .models import Category, Course, Module, Lesson
from users.serializers import TeacherSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id',]

class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['id', 'module', 'title', 'content', 'video_url', 'duration', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class ModulesSerializer(serializers.ModelSerializer):
    lessons = LessonSerializer(many=True)
    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'description', 'order', 'lessons', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class CourseSerializer(serializers.ModelSerializer):
    category = CategoryShortSerializer()
    modules = ModulesSerializer(many=True, write_only=True)
    teacher = TeacherSerializer()
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'category', 'price', 'discount_price', 'image', 'is_published', 'modules', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']