import datetime
from django.db import models
from django.utils import timezone

# Create your models here.

class Question(models.Model):

    # def __str__(self):
    #     return self.question_text

    # def was_published_recently(self):
    #     return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):

    # def __str__(self):
    #     return self.choice_text

    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

class Coin(models.Model):

    coin_name = models.CharField(max_length=30)
    coin_price = models.IntegerField()
    created_at = models.DateField()

    def __str__(self):
        return self.coin_name


class Customer(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)

    class Meta:
        ordering = ('created',)

