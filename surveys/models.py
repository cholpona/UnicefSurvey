from django.db import models
from location.models import City
from django.contrib.auth.models import User

ANSWER_CHOICES = (
    ('yes', 'Yes'),
    ('no', 'No'),
    ('maybe', 'Maybe'),
)

GENDER_CHOICES = (
    ('', 'Not defined'),
    ('M', 'Male'),
    ('F', 'Female'),
)

# Create your models here.
class Survey(models.Model):
    title = models.CharField(requried=True, max_length=255)
    start_date = models.DateField(requried=True)
    end_date = models.DateField(requried=True)


class SurveyCity(models.Model):
    survey = models.ForeignKey(Survey, requried=True)
    city = models.ForeignKey(City, requried=True)


class Question(models.Model):
    survey = models.ForeignKey(Survey, requried=True)
    text = models.CharField(max_length=255)


class Poll(models.Model):
    survey = models.ForeignKey(Survey)
    user = models.ForeignKey(User)
    gender = models.CharField(choices=GENDER_CHOICES)
    age = models.IntegerField()
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)

class Answer(models.Model):
    poll = models.ForeignKey(Poll)
    question = models.ForeignKey(Question)
    answer = models.CharField(choices=ANSWER_CHOICES)
