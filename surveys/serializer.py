from rest_framework import serializers

from .models import *


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('url', 'text')

class SurveyCitySerializer(serializers.ModelSerializer):
    class Meta:
        model = SurveyCity
        fields = ('survey','city')

