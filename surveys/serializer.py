from rest_framework import serializers

from .models import *


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ('id', 'text')


class SurveySerializer(serializers.ModelSerializer):
    class Meta:
        model = Survey
        fields = ('id', 'title', )


class SurveyCitySerializer(serializers.ModelSerializer):
    survey = SurveySerializer()
    class Meta:
        model = SurveyCity
        fields = ('survey', 'city',)
