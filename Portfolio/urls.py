from django.urls import path
from .views import AboutView, AdminContactView, AdminEmailView, SocialIconView, ExperienceView, EducationView, ProgrammingLanguagesAndToolsView, ProjectView

urlpatterns = [
    path("about/", AboutView.as_view(), name="about-admin-api"),
    path("contacts/", AdminContactView.as_view(), name="admin-contacts-api"),
    path("emails/", AdminEmailView.as_view(), name="admin-emails-api"),
    path("social-icons/", SocialIconView.as_view(), name="admin-social-icons-api"),
    path("experiences/", ExperienceView.as_view(), name="admin-experience-api"),
    path("educations/", EducationView.as_view(), name="admin-education-api"),
    path("skills/", ProgrammingLanguagesAndToolsView.as_view(), name="admin-prog-langs-tools-api"),
    path("projects/", ProjectView.as_view(), name="admin-projects-api"),
]
