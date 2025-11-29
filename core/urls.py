
from django.contrib import admin
from django.urls import path


from projects.views.tag_views import TagListCreateAPIView, TagDetailApiView
from projects.views.project import ProjectDetailAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tags/', TagListCreateAPIView.as_view()),
    path('tags/<int:pk>/', TagDetailApiView.as_view()),
    path('project/<int:pk>',ProjectDetailAPIView.as_view() )

]
