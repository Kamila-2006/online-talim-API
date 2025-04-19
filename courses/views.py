from rest_framework import viewsets
from .models import Category, Course, Module, Lesson
from .serializers import CategorySerializer, CourseSerializer, ModulesSerializer
from .pagination import CategoryPagination, CoursePagination, ModulePagination, LessonPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModulesSerializer
    pagination_class = ModulePagination