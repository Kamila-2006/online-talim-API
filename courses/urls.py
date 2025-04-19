from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'categories', views.CategoryViewSet, basename='categories')
router.register(r'courses', views.CourseViewSet, basename='courses')
router.register(r'modules', views.ModuleViewSet, basename='modules')
router.register(r'lessons', views.LessonViewSet, basename='lessons')

urlpatterns = [
    path('', include(router.urls)),
]