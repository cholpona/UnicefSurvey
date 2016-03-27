<<<<<<< HEAD
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import UserSerializer
=======
import datetime
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.core.urlresolvers import reverse
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View
#from jose import jws
from rest_framework.decorators import api_view
from rest_framework.response import Response

from staff.models import Worker
from surveys.models import SurveyCity
from surveys.serializer import SurveyCitySerializer


class AuthenticationView(View):
    def post(self, request):
        credentials = self.request.GET.urlencode()
        # username = request.POST.get("username", "")
        # password = request.POST.get("password", "")
        username = credentials['username']
        password = credentials['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                expiry = datetime.date.today() + datetime.timedelta(days=50)
                #token = jws.sign({'username': user.username, 'expiry':expiry}, 'seKre8', algorithm='HS256')
                token = ""
                return HttpResponse(token)
            else:
                print("The password is valid, but the account has been disabled!")
        else:
            html = "<html><body>Fail.</body></html>"
            return HttpResponse(html)


class SurveyCitiesList(View):
    def post(self,request):
        worker = self.request.GET("user")
        survey_city_list = SurveyCity.objects.filter(city__exact=worker.city)






>>>>>>> f14bf508d18d0bc9309a76ff05b85c87064c014e


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
