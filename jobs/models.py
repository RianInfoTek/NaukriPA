from django.conf import settings
from django.db import models

class JobDescription(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)
    job_type = models.CharField(max_length=50, blank=True, null=True)  # e.g., Full-time, Part-time
    job_description = models.TextField()
    skills_required = models.TextField(blank=True, null=True)
    experience_level = models.CharField(max_length=50, blank=True, null=True)  # e.g., Entry-level, Mid-level
    industry = models.CharField(max_length=255, blank=True, null=True)
    salary_range = models.CharField(max_length=100, blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    posted_date = models.DateTimeField(auto_now_add=True)


# Create your models here.
