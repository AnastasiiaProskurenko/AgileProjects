from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework import status

from projects.models import Task
from projects.serializers import AllTaskSerialiser,CreateTaskSerializer

class AllTaskListView(ListCreateAPIView):
    queryset = Task.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return AllTaskSerialiser
        return CreateTaskSerializer



