from django.contrib import admin
from .models import About, AdminContact, AdminEmail, SocialIcon, Experience, Education, ProgrammingLanguagesAndTools, Project
# Register your models here.
admin.site.register(About)
admin.site.register(AdminContact)
admin.site.register(AdminEmail)
admin.site.register(SocialIcon)
admin.site.register(Experience)
admin.site.register(Education)
admin.site.register(ProgrammingLanguagesAndTools)
admin.site.register(Project)