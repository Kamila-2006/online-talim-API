from rest_framework.pagination import PageNumberPagination


class CategoryPagination(PageNumberPagination):
    page_size = 10

class CoursePagination(PageNumberPagination):
    page_size = 10

class ModulePagination(PageNumberPagination):
    page_size = 10

class LessonPagination(PageNumberPagination):
    page_size = 10