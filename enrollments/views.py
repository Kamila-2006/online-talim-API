from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from users.permissions import IsOwnerOrAdmin, IsEnrollmentOwnerOrAdmin, IsEnrollmentOwnerOrTeacherOrAdmin, IsCourseTeacherOrAdmin
from .models import Enrollment, Progress
from courses.models import Lesson
from .seralizers import EnrollmentSerializer, ProgressSerializer, EnrollmentDetailSerializer
from .pagination import EnrollmentPagination, ProgressPagination


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.all()
    pagination_class = EnrollmentPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            if self.action == 'list':
                return [IsAdminUser()]
            return [IsEnrollmentOwnerOrTeacherOrAdmin()]
        elif self.request.method == 'POST':
            return [IsAuthenticated()]
        elif self.request.method in ['PUT', 'PATCH']:
            return [IsEnrollmentOwnerOrTeacherOrAdmin()]
        elif self.request.method == 'DELETE':
            return [IsEnrollmentOwnerOrAdmin()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return EnrollmentDetailSerializer
        return EnrollmentSerializer

class EnrollmentsByUsers(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    pagination_class = EnrollmentPagination
    permission_classes = [IsOwnerOrAdmin]

    def get_queryset(self):
        user_id = self.kwargs['user_id']
        return Enrollment.objects.filter(user_id=user_id)

class EnrollmentsByCourses(generics.ListAPIView):
    serializer_class = EnrollmentSerializer
    pagination_class = EnrollmentPagination
    permission_classes = [IsCourseTeacherOrAdmin]

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

    def list(self, request, *args, **kwargs):
        response = super().list(request, *args, **kwargs)

        enrollment_id = self.kwargs['enrollment_id']
        enrollment = Enrollment.objects.get(id=enrollment_id)
        course = enrollment.course

        total_lessons = Lesson.objects.filter(module__course=course).count()
        completed_lessons = Progress.objects.filter(enrollment=enrollment, is_completed=True).count()
        percentage = int((completed_lessons / total_lessons) * 100) if total_lessons else 0

        response.data["progress_summary"] = {
            "completed_lessons": completed_lessons,
            "total_lessons": total_lessons,
            "percentage": percentage
        }
        return response