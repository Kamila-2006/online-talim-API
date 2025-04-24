from django.contrib import admin
from .models import Enrollment


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'course', 'enrolled_at', 'is_completed', 'completed_at')
    search_fields = ('user', 'course', 'enrolled_at')