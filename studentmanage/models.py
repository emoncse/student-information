from django.db import models

# Create your models here.


class StudentBasicInfo(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    student_id = models.CharField(max_length=100, blank=True, null=True)
    phone = models.CharField(max_length=17, blank=True, null=True)
    email = models.EmailField(max_length=70, blank=True, null=True)
