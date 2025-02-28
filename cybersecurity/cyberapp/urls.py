from django.contrib import admin
from django.urls import path
from .views import incident_response,analyze_threat,analyze_log,incident_file # Import views from your app

urlpatterns = [
    path('analyze/', analyze_threat, name='analyze_threat'),  # Threat analysis
    path('upload-log/', analyze_log, name='analyze_log'),  # Log file analysis
    path('incident/', incident_response, name='incident_response'),  # Incident response
    path('incidentfile',incident_file,name='incident_file'), # Incident file
]
