from django.contrib import admin
from .models import Project, Resume, Profile

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'github_link', 'live_demo')

admin.site.register(Resume)
admin.site.register(Profile)
