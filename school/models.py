from django.db import models

# Create your models here.
class Student(models.Model):
    """A student in the scholl"""
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name
