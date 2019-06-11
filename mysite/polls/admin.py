from django.contrib import admin

from .models import Question

class QuesitonAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Data information', {'fields': ['pub_date']}),
    ]

admin.site.register(Question, QuesitonAdmin)
