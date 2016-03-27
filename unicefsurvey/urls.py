from django.conf.urls import patterns, include, url
from django.contrib import admin

from surveys.views import *
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'question', QuestionViewSet)
router.register(r'survey', SurveyViewSet)
router.register(r'answer', AnswerViewSet)
# router.register(r'questions', QuestionList, 'Question')
# router.register(r'questions/(?P<pk>[0-9]+)', QuestionDetail, 'Detail')

# router.register(r'snippets/', question_list)
# router.register(r'snippets/(?P<pk>[0-9]+)', question_detail)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unicefsurvey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include(router.urls)),
    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^staff/', include('staff.urls')),

    url(r'^submit', "surveys.views.ParsePoll", name='submit'),

)
