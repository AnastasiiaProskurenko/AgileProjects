from django.db import models
from django.core.validators import MinLengthValidator

from .project import Project

# Создайте модель Task со следующими полями:
# Название задачи: строковое поле, уникальное, минимальная длина названия - 10 символов
# Описание: большое строковое поле, может быть пустым
# Статус: строковое поле максимальной длины в 15 символов, должно быть полем выбора разных статусов. По умолчанию все задачи новые
# Приоритет: строковое поле максимальной длины в 15 символов, должно быть полем выбора разных приоритетов
# Проект: связь с моделью Project, при удалении проекта все задачи должны удаляться
# Дата создания задачи: поле, поддерживающее и дату, и время, заполняется автоматически только при создании
# Дата обновления: поле, поддерживающее и дату, и время, заполняется автоматически всегда
# Дата удаления: поле, в котором может ничего не быть

list_status = [
    ('new', 'Новая'),
    ('in_progress', 'В процессе'),
    ('blocked', 'Заблокирована'),
    ('pending', 'Приостановлена'),
    ('testing', 'Тестирование'),
    ('inreview', 'На проверке'),
    ('done', 'Завершена'),
]

priority_status = [
    ('5', 'Немедленный'),
    ('4', 'Главный'),
    ('3', 'Высокий'),
    ('2', 'Средний'),
    ('1', 'Низкий'),
]


class Tag(models.Model):
    title = models.CharField(max_length=25, unique=True)
    parent = models.ForeignKey("self", on_delete=models.CASCADE, related_name="children")  # todo:manytomany!

    def __str__(self):
        return self.title

class Task(models.Model):
    title = models.CharField(max_length=10, unique=True, validators=[MinLengthValidator(10)])
    description = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=15, choices=list_status, default="new")
    priority = models.CharField(max_length=15, choices=priority_status)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at =models.DateTimeField(auto_now_add=True)
    deleted_at = models.DateTimeField(null=True, blank=True)
    due_date = models.DateField(blank=True, null=True)
    tags = models.ManyToManyField("Tag", related_name="tasks")

    def __str__(self):
        return self.priority


# Расширьте модель Task дополнительным хранением тегов:
# Создайте модель тегов (Tag):
# Имя тэга (Строковое поле, уникальное)
# Добавьте поле due_date (срок выполнения) в модель Task.
# Свяжите модель Задачи с тегами через связь “Многие ко многим”, добавив в модель задачи новое поле tags

