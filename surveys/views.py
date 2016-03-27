from rest_framework.response import Response
from rest_framework import viewsets
from .models import *
from staff.models import Worker
from .serializer import SurveyCitySerializer
from .serializer import QuestionSerializer
from rest_framework.decorators import api_view
#  Create your views here.


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


@api_view()
def getSurveyList(request):
    list = SurveyCity.objects.filter(city=request.user.worker.city)
    serializer = SurveyCitySerializer(list, many=True)
    return Response(serializer.data)