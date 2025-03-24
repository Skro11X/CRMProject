from django.contrib import admin
from leads.models import Lead

@admin.register(Lead)
class LeadAdmin(admin.ModelAdmin):
    pass
# Register your models here.
