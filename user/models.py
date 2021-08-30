from django.db import models
from django.utils.timezone import now

class User(models.Model):
    name = models.CharField(max_length=32)
    username = models.CharField(max_length=16,unique=True)
    password = models.CharField(max_length=20)
    entity = models.IntegerField(default=1)
    status = models.SmallIntegerField(default=1)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class Meta:
    db_table = 'User'

class Task(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=128,default=1)
    description = models.CharField(max_length=20,default=1)
    date = models.DateTimeField()
    status = models.SmallIntegerField(default=1)
    created_date = models.DateTimeField(default=now)
    updated_by = models.IntegerField(null=True, blank=True)
    updated_date = models.DateTimeField(null=True, blank=True)

class Meta:
    db_table = 'Task'
