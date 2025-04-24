from django.contrib import admin
from .models import Enrollment, Progress


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'enrolled_at', 'is_completed', 'completed_at')
    search_fields = ('user', 'course', 'enrolled_at')

@admin.register(Progress)
class ProgressAdmin(admin.ModelAdmin):
    list_display = ('id', 'enrollment', 'lesson', 'is_completed', 'completed_at')
    search_fields = ('enrollment', 'lesson', 'is_completed')