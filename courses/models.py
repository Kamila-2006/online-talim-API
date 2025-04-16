from django.db import models
from users.models import User
from categories.models import Category


class CourseModel(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='courses')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='courses')
    price = models.DecimalField(max_digits=13, decimal_places=2)
    discount_price = models.DecimalField(max_digits=13, decimal_places=2, null=True)
    image = models.ImageField(upload_to='course-images', blank=True, null=True)
    is_published = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)