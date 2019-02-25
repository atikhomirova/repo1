from datetime import datetime
from django.db import models

class Todo(models.Model):
    # Ant: Add in the model field date of close, using migrations

    title = models.CharField(max_length=200)
    text = models.TextField()
    created_at = models.DateTimeField(default=datetime.now())
    closed_at = models.DateTimeField(blank=True, null=True)
    is_done = models.BooleanField(default=0)

    def __str__(self):
        return self.title
