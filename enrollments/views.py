from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Enrollment, Progress
from .seralizers import EnrollmentSerializer, ProgressSerializer
from .pagination import EnrollmentPagination, ProgressPagination


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer
    pagination_class = EnrollmentPagination
    permission_classes = [IsAuthenticated]

class EnrollmentsByUsers(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    pagination_class = EnrollmentPagination

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Enrollment.objects.filter(user_id=user_id)

class EnrollmentsByCourses(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    pagination_class = EnrollmentPagination

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Enrollment.objects.filter(course_id=course_id)

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer
    pagination_class = ProgressPagination

class ProgressByEnrollment(generics.ListAPIView):
    serializer_class = ProgressSerializer
    pagination_class = ProgressPagination

    def get_queryset(self):
        enrollment_id = self.kwargs['enrollment_id']
        return Progress.objects.filter(enrollment_id=enrollment_id)