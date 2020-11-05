from django.shortcuts import render
from .serializers import AboutSerializer, AdminContactSerializer, AdminEmailSerialiazer, SocialIconSerialiazer, ExperienceSerialiazer, EducationSerialiazer, ProgrammingLanguagesAndToolsSerialiazer, ProjectSerialiazer
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.permissions import IsAdminUser
from .models import About, AdminContact, AdminEmail, SocialIcon, Experience, Education, ProgrammingLanguagesAndTools, Project
from rest_framework.response import Response
# Create your views here.
class AboutView(ListAPIView):
    serializer_class = AboutSerializer
    queryset = About.objects.all()

class AdminContactView(ListAPIView):
    serializer_class = AdminContactSerializer
    queryset = AdminContact.objects.all()

class AdminEmailView(ListAPIView):
    serializer_class = AdminEmailSerialiazer
    queryset = AdminEmail.objects.all()

class AdminEmailView(ListAPIView):
    serializer_class = AdminEmailSerialiazer
    queryset = AdminEmail.objects.all()
    
class SocialIconView(ListAPIView):
    serializer_class = SocialIconSerialiazer
    queryset = SocialIcon.objects.all()
    
class ExperienceView(ListAPIView):
    serializer_class = ExperienceSerialiazer
    queryset = Experience.objects.all()
    
class EducationView(ListAPIView):
    serializer_class = EducationSerialiazer
    queryset = Education.objects.all()
    
class ProgrammingLanguagesAndToolsView(ListAPIView):
    serializer_class = ProgrammingLanguagesAndToolsSerialiazer
    queryset = ProgrammingLanguagesAndTools.objects.all()
    
class ProjectView(ListAPIView):
    serializer_class = ProjectSerialiazer
    queryset = Project.objects.all()

# class ListUsers(APIView):
#     permission_classes = [IsAdminUser]
#     def get(self, request, format=None):
#         obj = About.objects.first()

#         return Response(obj)
