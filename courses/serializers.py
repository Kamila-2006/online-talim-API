from rest_framework import serializers
from .models import Category, Course, Module, Lesson
from users.models import User
from users.serializers import TeacherSerializer


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'description', 'icon', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

class CategoryShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']
        read_only_fields = ['id',]

class LessonModuleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Module
        fields = ['id', 'title']
        read_only_fields = ['id', 'title']

class LessonSerializer(serializers.ModelSerializer):
    module = LessonModuleSerializer(read_only=True)
    class Meta:
        model = Lesson
        fields = ['id', 'module', 'title', 'content', 'video_url', 'duration', 'order', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['module'] = LessonModuleSerializer(instance.module).data
        return rep

class LessonShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = ['title', 'content', 'video_url', 'duration', 'order']

class ModulesSerializer(serializers.ModelSerializer):
    lessons = LessonShortSerializer(many=True, write_only=True)
    class Meta:
        model = Module
        fields = ['id', 'course', 'title', 'description', 'order', 'lessons', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        lessons_data = validated_data.pop('lessons', [])

        module = Module.objects.create(**validated_data)

        for lesson_data in lessons_data:
            Lesson.objects.create(module=module, **lesson_data)

        return module

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['course'] = CourseShortSerializer(instance.course).data
        return rep

class ModulesShortSerializer(serializers.ModelSerializer):
    lessons = LessonShortSerializer(many=True, write_only=True)
    class Meta:
        model = Module
        fields = ['title', 'description', 'order', 'lessons']

class CourseSerializer(serializers.ModelSerializer):
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    modules = ModulesShortSerializer(many=True, write_only=True)
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(is_teacher=True))

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'category', 'price', 'discount_price', 'image', 'is_published', 'modules', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        modules_data = validated_data.pop('modules', [])
        category = validated_data.pop('category', None)
        teacher = validated_data.pop('teacher')

        course = Course.objects.create(teacher=teacher, category=category, **validated_data)

        for module_data in modules_data:
            lessons_data = module_data.pop('lessons', [])
            module = Module.objects.create(course=course, **module_data)
            for lesson_data in lessons_data:
                Lesson.objects.create(module=module, **lesson_data)

        return course

    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['teacher'] = TeacherSerializer(instance.teacher).data
        rep['category'] = CategoryShortSerializer(instance.category).data
        return rep

class CourseShortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title']
        read_only_fields = ['id',]