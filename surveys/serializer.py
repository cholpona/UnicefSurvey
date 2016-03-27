from rest_framework import serializers

from .models import *


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('url', 'text')



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
>>>>>>> f14bf508d18d0bc9309a76ff05b85c87064c014e
