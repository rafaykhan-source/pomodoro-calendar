from django.contrib import admin

from .models import Session, Task, Note, SessionTaskContainer

admin.site.register(Session)
admin.site.register(Task)
admin.site.register(SessionTaskContainer)
admin.site.register(Note)
