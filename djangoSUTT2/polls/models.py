from django.utils import timezone
import datetime
from django.contrib import admin
from django.db import models #models allows us to define models that map to database tables
class Question(models.Model):#models.Model means that Question is a Django model and will be stored in a database
    question_text=models.CharField(max_length=200)
    pub_date=models.DateTimeField("date published")# date published is the human readable name for this field
    def __str__(self):
        return self.question_text
    @admin.display(
        boolean=True,
        ordering="pub_date",
        description="Published recently?",
    )
    def was_published_recently(self):
        now = timezone.now()
        return now-datetime.timedelta(days=1) <= self.pub_date <= now
class Choice(models.Model):
    question=models.ForeignKey(Question, on_delete=models.CASCADE)# creates a foreign key connecting the choice to a question and on delete means that if a question is deleted we will delete all related choices also
    choice_text=models.CharField(max_length=200)# creates a text field called choice_texts
    votes= models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text

# Create your models here.
# a django project is like the whole web application example Facebook app but the app is a single application like the messenger,  Notifications, News feed etc
# our project here is mysite, polls is an app
# we need to tell project about our app 
# 