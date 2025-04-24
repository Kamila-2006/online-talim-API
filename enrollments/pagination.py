from rest_framework.pagination import PageNumberPagination


class EnrollmentPagination(PageNumberPagination):
    page_size = 10

class ProgressPagination(PageNumberPagination):
    page_size = 10