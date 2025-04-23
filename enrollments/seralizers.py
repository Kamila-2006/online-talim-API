from rest_framework import serializers
from .models import Enrollment
from users.serializers import UserShortSerializer
from courses.serializers import CourseShortSerializer


class EnrollmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'is_completed', 'completed_at', 'enrolled_at']
        read_only_fields = ['id', 'enrolled_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserShortSerializer(instance.user).data
        rep['course'] = CourseShortSerializer(instance.course).data
        return rep