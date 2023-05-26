from rest_framework import viewsets
from .models import Task, Session, Note, SessionTaskContainer
from .serializers import (
    TaskSerializer,
    SessionSerializer,
    NoteSerializer,
    SessionTaskContainerSerializer
)


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """

    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class SessionViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows sessions to be viewed or edited.
    """

    queryset = Session.objects.all()
    serializer_class = SessionSerializer


class NoteViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows notes to be viewed or edited.
    """

    queryset = Note.objects.all()
    serializer_class = NoteSerializer


class SessionTaskContainerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows session task containers to be viewed or edited.
    """

    queryset = SessionTaskContainer.objects.all()
    serializer_class = SessionTaskContainerSerializer
