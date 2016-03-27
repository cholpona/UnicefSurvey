from datetime import date

from rest_framework.response import Response
from rest_framework import viewsets
from .models import *

from staff.models import Worker
from .serializer import *
from .serializer import SurveyCitySerializer
from .serializer import QuestionSerializer
from .serializer import SurveySerializer
from rest_framework.decorators import api_view

#  Create your views here.
from rest_framework.views import APIView
from django.http import Http404, HttpResponse


class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class SurveyViewSet(viewsets.ModelViewSet):
    queryset = Survey.objects.all()
    serializer_class = SurveySerializer


class AnswerViewSet(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer




def ParsePoll(request):

    json = {
        "survey_id": 1,
        "gender": "F",
        "age": 20,
        "lat": 1,
        "lng": 1,
        "questions": [{
            "question_id": 1,
            "answer": "yes"
        }, {
            "question_id": 2,
            "answer": "no"
        }]
    }
    survey_id = json["survey_id"]
    survey = Survey.objects.get(id=survey_id)

    gender = json["gender"]
    age = json["age"]
    lat, lan = json["lat"], json["lng"]

    poll = Poll(survey=survey,
                gender=gender,
                age=age,
                lat=lat, lng=lan)
    poll.save()
    questions = json["questions"]

    for question in questions:
        id = question["question_id"]
        question_object = Question.objects.get(id=id)
        question_answer = question["answer"]
        answer = Answer(poll=poll,
                        question=question_object,
                        answer=question_answer)
        answer.save()

    return HttpResponse("<h1>Ok</h1>")


@api_view()
def getSurveyList(request):
    list = SurveyCity.objects.filter(city=request.user.worker.city,is_Active=True,start_date__lte=date.today(), end_date__gre=date.today())
    serializer = SurveyCitySerializer(list, many=True)
    return Response(serializer.data)


@api_view()
def getSurveyQuestions(request,pk):
    list = Question.objects.filter(survey__pk =pk)
    serializer = QuestionSerializer(list,many=True)
    return Response(serializer.data)

