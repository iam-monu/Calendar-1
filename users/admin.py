from django.contrib import admin
from .models import Events #EventName
from .models import Customer


class AdminDashboard(admin.ModelAdmin):
    list_display = ['title', 'meet_id', 'start_time', 'end_time','user']



# Register your models here.
admin.site.register(Events, AdminDashboard)
admin.site.register(Customer)