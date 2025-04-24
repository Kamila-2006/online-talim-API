from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'enrollments', views.EnrollmentViewSet, basename='enrollments')
router.register(r'progress', views.ProgressViewSet, basename='progress')

urlpatterns = [
    path('', include(router.urls)),
    path('enrollments/users/<int:user_id>/', views.EnrollmentsByUsers.as_view()),
    path('enrollments/courses/<int:course_id>/', views.EnrollmentsByCourses.as_view()),
]