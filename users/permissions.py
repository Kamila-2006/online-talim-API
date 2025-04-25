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

class IsEnrollmentOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        enrollment_id = request.data.get('enrollment') or request.query_params.get('enrollment')
        if not enrollment_id:
            return False
        return Enrollment.objects.filter(id=enrollment_id, user=request.user).exists()

class IsProgressOwner(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.enrollment.user == request.user

class IsProgressOwnerOrTeacherOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        user = request.user
        return (
            user.is_authenticated and (
                obj.enrollment.user == user or
                obj.enrollment.course.teacher == user or
                user.is_staff
            )
        )

