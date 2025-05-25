from rest_framework import viewsets
from .models import Project, Resume, Profile
from .serializers import ProjectSerializer, ResumeSerializer, ProfileSerializer
from django.core.mail import send_mail
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

@csrf_exempt
def contact_view(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)

            name = data.get('user_name')
            email = data.get('user_email')
            message = data.get('message')

            if not all([name, email, message]):
                return JsonResponse({'error': 'Missing fields'}, status=400)

            full_message = f"From: {name} <{email}>\n\nMessage:\n{message}"

            send_mail(
                subject='Portfolio Contact Form',
                message=full_message,
                from_email='your-email@example.com',
                recipient_list=['your-email@example.com'],
                fail_silently=False,
            )

            return JsonResponse({'success': True})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Invalid method'}, status=405)

