from django.contrib import admin

from .models import Session, Task, SessionTaskContainer

admin.site.register(Session)
admin.site.register(Task)
admin.site.register(SessionTaskContainer)
