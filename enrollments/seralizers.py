from rest_framework import serializers
from .models import Enrollment
from courses.models import Course
from users.serializers import UserShortSerializer
from courses.serializers import CourseShortSerializer


class EnrollmentSerializer(serializers.ModelSerializer):
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Enrollment
        fields = ['id', 'user', 'course', 'is_completed', 'completed_at', 'enrolled_at']
        read_only_fields = ['id', 'user', 'enrolled_at']

    def create(self, validated_data):
        user = self.context['request'].user
        return Enrollment.objects.create(user=user, **validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['user'] = UserShortSerializer(instance.user).data
        rep['course'] = CourseShortSerializer(instance.course).data
        return rep

class ProgressSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['id', 'enrollment', 'lesson', 'is_completed', 'completed_at']
        read_only_fields = ['id',]