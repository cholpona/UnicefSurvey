from django.db import models
from location.models import City
from staff.models import Worker

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
    title = models.CharField(blank=False, max_length=255)
    start_date = models.DateField()
    end_date = models.DateField()

    def __unicode__(self):
        return self.title


class SurveyCity(models.Model):
    survey = models.ForeignKey(Survey)
    city = models.ForeignKey(City)


class Question(models.Model):
    survey = models.ForeignKey(Survey)
    text = models.CharField(max_length=255)

    def __unicode__(self):
        return self.text


class Poll(models.Model):
    survey = models.ForeignKey(Survey)
    user = models.ForeignKey(Worker)
    gender = models.CharField(choices=GENDER_CHOICES, max_length=2)
    age = models.IntegerField()
    lat = models.CharField(max_length=255)
    lng = models.CharField(max_length=255)


class Answer(models.Model):
    poll = models.ForeignKey(Poll)
    question = models.ForeignKey(Question)
    answer = models.CharField(choices=ANSWER_CHOICES, max_length=2)
