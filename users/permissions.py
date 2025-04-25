from rest_framework import permissions
from enrollments.models import Enrollment


class IsOwnerOrAdminOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return request.user.is_authenticated
        return obj == request.user or request.user.is_staff

class IsTeacher(permissions.BasePermission):
    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.is_teacher)

class IsCourseTeacherOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return request.user.is_staff or (obj.teacher == request.user)

class IsEnrolledOrTeacherOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if not request.user or not request.user.is_authenticated:
            return False

        if request.user.is_staff:
            return True

        if obj.module.course.teacher == request.user:
            return True

        return Enrollment.objects.filter(user=request.user, course=obj.module.course).exists()

class IsEnrollmentOwnerOrTeacherOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and (
                request.user.is_staff or
                obj.user == request.user or
                obj.course.teacher == request.user
            )
        )

class IsEnrollmentOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return (
            request.user.is_authenticated and (
                request.user.is_staff or
                obj.user == request.user
            )
        )

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        user_id = view.kwargs.get('user_id')
        return (
            request.user.is_authenticated and (
                request.user.is_staff or
                str(request.user.id) == str(user_id)
            )
        )