from rest_framework import serializers
from .models import About, AdminContact, AdminEmail, SocialIcon, Experience, Education, ProgrammingLanguagesAndTools, Project

class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'

class AdminContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminContact
        fields = '__all__'

class AdminEmailSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = AdminEmail
        fields = '__all__'

class SocialIconSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = SocialIcon
        fields = '__all__'

class ExperienceSerialiazer(serializers.ModelSerializer):
    from_date = serializers.SerializerMethodField()
    to_date = serializers.SerializerMethodField()
    class Meta:
        model = Experience
        fields = '__all__'
    def get_from_date(self, obj):
        return obj.from_date.strftime("%B %Y")
    def get_to_date(self, obj):
        return obj.to_date.strftime("%B %Y")

class EducationSerialiazer(serializers.ModelSerializer):
    from_date = serializers.SerializerMethodField()
    to_date = serializers.SerializerMethodField()
    class Meta:
        model = Education
        fields = '__all__'
    def get_from_date(self, obj):
        return obj.from_date.strftime("%B %Y")
    def get_to_date(self, obj):
        return obj.to_date.strftime("%B %Y")

class ProgrammingLanguagesAndToolsSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = ProgrammingLanguagesAndTools
        fields = '__all__'

class ProjectSerialiazer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'