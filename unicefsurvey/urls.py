from django.conf.urls import patterns, include, url
from django.contrib import admin

from surveys.views import QuestionViewSet
from rest_framework import routers

router=routers.DefaultRouter()
router.register(r'question', QuestionViewSet)


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'unicefsurvey.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),


    url(r'^admin/', include(admin.site.urls), name='admin'),
    url(r'^staff/', include('staff.urls')),
    url(r'^', include(router.urls)),
)
