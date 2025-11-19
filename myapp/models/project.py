from django.db import models
from django.core.validators import MinLengthValidator

# Создайте модель Project со следующими полями:
# Название проекта: строковое, уникальное
# Описание проекта: строковое, большое поле, обязательно к заполнениюДата создания проекта: должна проставляться автоматически при создании
# Create your models here.
class Project(models.Model):
    title = models.CharField(
        max_length=255, unique=True
    )

    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)