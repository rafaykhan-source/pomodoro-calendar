from django.db import models


class Session(models.Model):
    name = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.start_time


class Task(models.Model):
    session = models.ForeignKey(Session, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
