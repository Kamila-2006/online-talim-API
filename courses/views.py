from rest_framework import viewsets
from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAdminUser, IsAuthenticated
from .models import Category, Course, Module, Lesson
from .serializers import CategorySerializer, CourseSerializer, CourseUpdateSerializer, ModulesSerializer, LessonSerializer, ModuleUpdateSerializer, LessonUpdateSerializer
from .pagination import CategoryPagination, CoursePagination, ModulePagination, LessonPagination
from users.permissions import IsTeacher, IsCourseTeacherOrAdmin, IsEnrolledOrTeacherOrAdmin


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    pagination_class = CategoryPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            return [AllowAny()]
        return [IsAdminUser()]

class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    def get_permissions(self):
        if self.request.method == 'POST':
            return [IsTeacher()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsCourseTeacherOrAdmin()]
        return [AllowAny()]

    def get_serializer_class(self):
        if self.action == 'create':
            return CourseSerializer
        elif self.action in ['update', 'partial_update']:
            return CourseUpdateSerializer
        return CourseSerializer

class CoursesByCategory(generics.ListAPIView):
    serializer_class = CourseSerializer
    pagination_class = CoursePagination

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        return Course.objects.filter(category_id=category_id)

class ModuleViewSet(viewsets.ModelViewSet):
    queryset = Module.objects.all()
    serializer_class = ModulesSerializer
    pagination_class = ModulePagination

    def get_permissions(self):
        if self.request.method == 'GET':
            return [IsAuthenticated()]
        return [IsCourseTeacherOrAdmin()]

    def get_serializer_class(self):
        if self.action == 'create':
            return ModulesSerializer
        elif self.action in ['update', 'partial_update']:
            return ModuleUpdateSerializer
        return ModulesSerializer

class ModulesByCourse(generics.ListAPIView):
    serializer_class = ModulesSerializer
    pagination_class = ModulePagination
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Module.objects.filter(course_id=course_id)

class LessonViewSet(viewsets.ModelViewSet):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
    pagination_class = LessonPagination

    def get_permissions(self):
        if self.request.method == 'GET':
            if self.action == 'list':
                return [IsAuthenticated()]
            return [IsEnrolledOrTeacherOrAdmin()]
        elif self.request.method == 'POST':
            return [IsCourseTeacherOrAdmin()]
        elif self.request.method in ['PUT', 'PATCH', 'DELETE']:
            return [IsCourseTeacherOrAdmin()]
        return [IsAuthenticated()]

    def get_serializer_class(self):
        if self.action == 'create':
            return LessonSerializer
        elif self.action in ['update', 'partial_update']:
            return LessonUpdateSerializer
        return LessonSerializer

class LessonsByModule(generics.ListAPIView):
    serializer_class = LessonSerializer
    pagination_class = LessonPagination
    permission_classes = [IsEnrolledOrTeacherOrAdmin]

    def get_queryset(self):
        module_id = self.kwargs['module_id']
        return Lesson.objects.filter(module_id=module_id)