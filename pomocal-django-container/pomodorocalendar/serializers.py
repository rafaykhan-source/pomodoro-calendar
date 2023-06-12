from rest_framework import serializers
from .models import Task, Note, Session, SessionTaskContainer


class SessionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Session
        fields = ("id", "name", "type", "start_time", "end_time", "completed")


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ("id", "name", "description", "completed")


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "name", "description")


class SessionTaskContainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = SessionTaskContainer
        fields = ("id", "session", "task")
