from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views


router = DefaultRouter()
router.register(r'reviews', views.ReviewViewSet, basename='reviews')

urlpatterns = [
    path('', include(router.urls)),
    path('reviews/course/<int:course_id>/', views.ReviewsByCourse.as_view(), name='reviews-by-course'),
    path('reviews/user/<int:user_id>/', views.ReviewsByUser.as_view(), name='reviews-by-user'),
]