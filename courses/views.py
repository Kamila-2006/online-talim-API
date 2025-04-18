from rest_framework import viewsets
from .models import Category, Course, Module, Lesson
from .serializers import CategorySerializer
from .pagination import CategoryPagination, CoursePagination, ModulePagination, LessonPagination


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination