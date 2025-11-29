from django.utils import timezone
from rest_framework import serializers
from projects.models import Task, Project, Tag


class AllTaskSerialiser(serializers.ModelSerializer):
    project=serializers.SlugRelatedField(
        slug_field="name",
        read_only=True
    )
    assignee=serializers.SlugRelatedField(
        slug_field="email",
        read_only=True
    )
    class Meta:
        model = Task
        fields = [
            'title',
            "status",
            'priority',
            'project',
            'assignee',
            'due_date'
        ]

class CreateTaskSerializer(serializers.ModelSerializer):
    projects=serializers.SlugRelatedField(
        slug_field="name",
        queryset=Project.objects.all()
    )

    class Meta:
        model = Task
        fields = [
            'title',
            'description',
            'priority',
            'project',
            'tags',
            'due_date'
        ]
    def validate_title(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Минимальная длина названия задачи, должна быть больше 10")
        return value

    def validate_description(self, value):
        if len(value) < 50:
            raise serializers.ValidationError("Минимальная длина описания задачи, должна быть больше 50")
        return value

    #def validate_priority(self, value):

    def validate_project_name(self, value):
        if not Project.objects.filter(name=value):
            raise serializers.ValidationError("Project not find")
        return value

    def validate_tags(self, value):
        if not Tag.objects.filter(id__in=value):
            raise serializers.ValidationError("Tag not find")
        return value

    def validate_due_date(self, value):
        time_data = timezone.make_aware(value,timezone.get_current_timezone())

        if time_data < timezone.now():
            raise serializers.ValidationError("Deadline can not be in past")
        return time_data









