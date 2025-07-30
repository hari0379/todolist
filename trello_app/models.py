from django.db import models
from django.utils import timezone
# Create your models here.
from django.contrib.auth.models import User

class TaskList(models.Model):
    name=models.CharField(max_length=100)
    created_at=models.DateTimeField(
        default=timezone.now
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} --- {self.created_at}'

class Task(models.Model):
    name=models.CharField(max_length=100)
    desc=models.TextField()
    created_at=models.DateTimeField(
        default=timezone.now()
    )
    due_date=models.DateTimeField()
    list=models.ForeignKey(TaskList,on_delete=models.CASCADE)
    def __str__(self):
        return f'{self.name} --- {self.desc}'






