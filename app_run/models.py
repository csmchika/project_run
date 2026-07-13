from django.db import models
from django.contrib.auth.models import User

class Run(models.Model):
    STATUS_CHOICES = [
        ('init', 'Запущен'),
        ('in_progress', 'Стартовал'),
        ('finished', 'Закончен'),
    ]

    created_at = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()
    athlete = models.ForeignKey(User, on_delete=models.CASCADE, related_name='athletes')
    status = models.TextField(choices=STATUS_CHOICES, default='init')


