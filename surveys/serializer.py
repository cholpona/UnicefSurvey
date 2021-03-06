from rest_framework import serializers

from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text')



class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('url', 'question', 'answer')


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'title', )


class SurveyCitySerializer(serializers.ModelSerializer):
    survey = SurveySerializer()
    class Meta:
        model = SurveyCity
        fields = ('survey', 'city',)
