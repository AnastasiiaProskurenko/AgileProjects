from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from projects.models import Project
from projects.serializers import ProjectDetailSerializer

class ProjectDetailAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()

    serializer_class = ProjectDetailSerializer

    # def update(self, request, *args, **kwargs):
    #     partial = False if request.method == "PUT" else True
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=partial)
    #     serializer.is_valid(raise_exception=True)
    #     self.perform_update(serializer)
    #     return Response(serializer.data)