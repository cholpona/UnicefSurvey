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


class QuestionList(viewsets.ModelViewSet):
    """
    List all questions, or create a new one.
    """
    def get_queryset(self):
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SurveyDetail(viewsets.ModelViewSet):
    """
    Retrieve, update or delete a snippet instance.
    """
    def get_object(self, pk):
        try:
            return Survey.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        survey = self.get_object(pk)
        serializer = QuestionSerializer(survey)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def question_list(request):
    """
    List all questions, or create a new one.
    """
    if request.method == 'GET':
        questions = Question.objects.all()
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def question_detail(request, pk):
    """
    Retrieve, update or delete a snippet instance.
    """
    try:
        question = Question.objects.get(pk=pk)
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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
    list = SurveyCity.objects.filter(city=request.user.worker.city)
    # surveylist = []
    # for surveycity in list:
    #     surveylist.append(surveycity.survey)
    serializer = SurveyCitySerializer(list, many=True)
    return Response(serializer.data)

