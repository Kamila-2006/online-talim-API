from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from users.permissions import IsReviewOwner, IsReviewOwnerOrAdmin, IsEnrolledAndCompleted, IsOwnerOrAdmin
from .models import Review
from .serializers import ReviewSerializer, ReviewUpdateSerializer
from .pagination import ReviewPagination


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        elif self.request.method == 'POST':
            return [IsAuthenticated(), IsEnrolledAndCompleted()]
        elif self.request.method in ['PUT', 'PATCH']:
            return [IsReviewOwner()]
        elif self.request.method == 'DELETE':
            return [IsReviewOwnerOrAdmin()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return ReviewSerializer
        elif self.action in ['update', 'partial_update']:
            return ReviewUpdateSerializer
        return ReviewSerializer

class ReviewsByCourse(generics.ListAPIView):
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    permission_classes = [AllowAny]

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Review.objects.filter(course_id=course_id)

class ReviewsByUser(generics.ListAPIView):
    serializer_class = ReviewSerializer
    pagination_class = ReviewPagination
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Review.objects.filter(user_id=user_id)