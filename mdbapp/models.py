from django.db import models
from django.contrib.auth.models import User


class TodoList(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=128,null=False,blank=False)
    todo = models.TextField(null=True,blank=True)

    class Meta:
        app_label = 'mdbapp'

    def __str__(self):

        return self.title