from django.contrib import admin
from .models import Events #EventName


class AdminDashboard(admin.ModelAdmin):
    list_display = ['title', 'meet_id', 'start_time', 'end_time','user']



# Register your models here.
admin.site.register(Events, AdminDashboard)