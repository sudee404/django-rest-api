from django.contrib import admin
from .models import Project, Service
# Register your models here.

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    '''Admin View for Service'''

    list_display = ('name','description')

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    '''Admin View for Project'''

    list_display = ('name','description','source_link',)
    list_filter = ('name','description',)