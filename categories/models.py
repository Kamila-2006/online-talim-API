from django.db import models


class Category:
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name