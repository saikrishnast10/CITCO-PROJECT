from django.contrib import admin
from mainpage.models import candidatemodel

# Register your models here.
class candidateadmin(admin.ModelAdmin):
    list_display=["Name","Email","Password","Gender","Qualification","Upload_Image","Upload_Resume"]
admin.site.register(candidatemodel,candidateadmin)