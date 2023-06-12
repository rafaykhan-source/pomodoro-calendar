# ----------------------------------------------------------------------
# urls.py
# ----------------------------------------------------------------------

from django.urls import include, path
from rest_framework import routers
from . import views

# ----------------------------------------------------------------------

router = routers.DefaultRouter()
router.register(r"tasks", views.TaskViewSet)
router.register(r"sessions", views.SessionViewSet)
router.register(r"notes", views.NoteViewSet)
router.register(r"sessiontaskcontainers", views.SessionTaskContainerViewSet)

# ----------------------------------------------------------------------

urlpatterns = [
    path("api/", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
