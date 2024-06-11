from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
        groups = models.ManyToManyField(
        'auth.Group',
        related_name='customuser_set',
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        verbose_name='groups'
    )
        user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='customuser_set',
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions'
    )

# class JobDescription(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Each job description is linked to a user
#     job_title = models.CharField(max_length=255)  # The job title
#     job_description = models.TextField()  # The full job description

# class ApplicationStatus(models.Model):
#     job = models.ForeignKey(JobDescription, on_delete=models.CASCADE)  # Each status is linked to a job description
#     status = models.CharField(max_length=255)  # The current status (e.g., applied, interviewed)
#     updated_at = models.DateTimeField(auto_now=True)  # Automatically set the field to now every time the object is saved


# Create your models here.
