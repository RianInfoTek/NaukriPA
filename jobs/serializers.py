from rest_framework import serializers
from .models import JobDescription

class JobDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobDescription
        fields = [
            'id', 'user', 'job_title', 'company_name', 'location', 'job_type', 
            'job_description', 'skills_required', 'experience_level', 'industry', 
            'salary_range', 'benefits', 'posted_date'
        ]
        read_only_fields = ['user', 'posted_date']