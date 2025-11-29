__all__ = [
    'ProjectDetailSerializer',
    'TagSerializer',
    'AllTaskSerialiser',
    'CreateTaskSerializer'
]

from projects.serializers.tag_serializers import TagSerializer
from projects.serializers.project import ProjectDetailSerializer
from projects.serializers.tasks_serializers import AllTaskSerialiser, CreateTaskSerializer