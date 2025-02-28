
from .parser import parse_data
from django.shortcuts import render
from .models import ThreatAnalysis

def threat_analysis_view(request):
    analysis = ThreatAnalysis.objects.all().order_by('-created_at')  # Fetch all analyses, newest first
    return render(request, 'threat_analysis.html', {'analysis': analysis})


def analyze_threat(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')

        analysis=parse_data(input_text)
        return render(request, 'cyberapp/result.html', {'analysis': analysis})
    return render(request, 'cyberapp/analyze.html')

def analyze_log(request):
    if request.method == 'POST' and request.FILES['log_file']:
        log_file = request.FILES['log_file']
        log_content = log_file.read().decode('utf-8')

        result=parse_data(log_content)
        return render(request, 'cyberapp/log_result.html', {'result': result})
    return render(request, 'cyberapp/upload_log.html')

def incident_response(request):
    if request.method == 'POST':
        incident_type = request.POST.get('incident_type')

        steps=parse_data(incident_type)
        return render(request, 'cyberapp/response_steps.html', {'steps': steps})
    return render(request, 'cyberapp/incident.html')
def incident_file(request):
    return render(request, 'cyberapp/incident.html')

