from django.contrib import admin
from myapp.models import Project, Task, Tag
# Register your models here.


# from django.template.library import TagHelperNode

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)
    list_filter = ('created_at',)

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'project', 'created_at', 'due_date', 'priority',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    search_fields = ('title',)