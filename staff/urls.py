from django.conf.urls import url

from . import views
urlpatterns = [
    #url(r'^authenticate/$', views.AuthenticationView.as_view(), name='authenticate'),
    url(r'^api-token-auth/', 'rest_framework_jwt.views.obtain_jwt_token'),


]