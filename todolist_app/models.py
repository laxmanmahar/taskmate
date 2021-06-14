from django.db import models
from django.db.models.fields import BooleanField, CharField
from django.contrib.auth.models import User


class TaskList(models.Model):
    manage = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    task = CharField(max_length=300, null=True, blank=True)
    done = BooleanField(default=False)

    def __str__(self):
        return self.task + " - " + str(self.done)
