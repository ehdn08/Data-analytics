from django.contrib import admin
from .models import Tag, UserReport, ScamRecord

# Register your models here.

admin.site.register(Tag)
admin.site.register(UserReport)
admin.site.register(ScamRecord)