from django.db import models


class ThreatAnalysis(models.Model):
    # Fields for the analysis data
    incident_report = models.CharField(max_length=255)
    date_of_incident = models.DateField()
    reported_by = models.CharField(max_length=100)
    priority_level = models.CharField(max_length=50, choices=[("Low", "Low"), ("Medium", "Medium"), ("High", "High")])
    summary = models.TextField()

    # Timestamp for record creation
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.incident_report} ({self.date_of_incident})"
