from django.db import models

class Task(models.Model):
    title = models.CharField('название', max_length=50)
    task = models.TextField('ОПИСАНИЕ')
    def __str__(self):
        return self.title

# Create your models here.
