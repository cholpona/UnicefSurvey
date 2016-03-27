from django.contrib import admin

# Register your models here.
from .models import *
from unicefsurvey.settings import *

from unicefsurvey.settings import *

class QuestionInline(admin.TabularInline):
    model = Question
    extra = QUESTION_PER_SURVEY

class QuestionAdmin(admin.ModelAdmin):
    list_display = ['text', 'survey__title']


class SurveyAdmin(admin.ModelAdmin):
    list_display = ['title', 'start_date', 'end_date','statistics_link']
    inlines = [
        QuestionInline,
    ]
    def statistics_link(self, obj):
        return "<a href='%s' target='_blank'>%s</>" % ("link", ("View statistics"))
    statistics_link.allow_tags = True

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('poll', 'question' ,'answer')
    class Meta:
        model = Answer

admin.site.register(Answer, AnswerAdmin)
admin.site.register(Poll)
admin.site.register(Survey, SurveyAdmin)
admin.site.register(Question)
admin.site.register(SurveyCity)
