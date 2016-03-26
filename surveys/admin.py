from django.contrib import admin

# Register your models here.
from .models import *
from unicefsurvey.settings import *


class QuestionInline(admin.TabularInline):
    model = Question
    extra = QUESTION_PER_SURVEY

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'survey__title']


class SurveyAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date']
    inlines = [
        QuestionInline,
    ]


admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)
admin.site.register(SurveyCity)
