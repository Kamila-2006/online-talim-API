from rest_framework import serializers
from .models import Enrollment, Progress
from courses.models import Course
from users.serializers import UserShortSerializer
from courses.serializers import CourseShortSerializer, ProgressLessonSerializer


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

class EnrollmentShortSerializer(serializers.ModelSerializer):
    course = CourseShortSerializer(read_only=True)
    class Meta:
        model = Enrollment
        fields = ['id', 'course']
        read_only_fields = ['id', 'course']

class ProgressSerializer(serializers.ModelSerializer):
    enrollment = EnrollmentShortSerializer(read_only=True)
    lesson = ProgressLessonSerializer(read_only=True)

    class Meta:
        model = Progress
        fields = ['id', 'enrollment', 'lesson', 'is_completed', 'completed_at']
        read_only_fields = ['id',]

class EnrollmentDetailSerializer(EnrollmentSerializer):
    progress = serializers.SerializerMethodField()

    class Meta(EnrollmentSerializer.Meta):
        fields = EnrollmentSerializer.Meta.fields + ['progress']

    def get_progress(self, obj):
        from courses.models import Lesson

        total_lessons = Lesson.objects.filter(module__course=obj.course).count()
        completed_lessons = Progress.objects.filter(
            enrollment=obj, is_completed=True
        ).count()

        percentage = int((completed_lessons / total_lessons) * 100) if total_lessons else 0

        return {
            "completed_lessons": completed_lessons,
            "total_lessons": total_lessons,
            "percentage": percentage
        }