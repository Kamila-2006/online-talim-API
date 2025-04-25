from rest_framework import serializers
from .models import Review
from courses.models import Course
from users.serializers import UserShortSerializer
from courses.serializers import CourseShortSerializer


class ReviewSerializer(serializers.ModelSerializer):
    user = UserShortSerializer(read_only=True)
    course = serializers.PrimaryKeyRelatedField(queryset=Course.objects.all())

    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'rating', 'comment', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        user = self.context['request'].user
        return Review.objects.create(user=user, **validated_data)

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['course'] = CourseShortSerializer(instance.course).data
        return rep