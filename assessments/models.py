from django.db import models
from acc.models import User
from courses.models import CourseModel, LessonModel
from django.urls import reverse
import datetime

from django.db import models
from django.utils import timezone

class Quiz(models.Model):
    lesson = models.ForeignKey(LessonModel,on_delete=models.CASCADE,default=None, related_name='lesson_test')
    title = models.CharField(max_length=1000)
    instructions = models.TextField(help_text='*learning objectives*')
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)
 
    def __unicode__(self):
        return self.title

    def __str__(self): #for python3
        return self.title 
    
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
    
    def get_absolute_url(self):
        return reverse("assessment:test", kwargs={"pk": self.pk})
    
class QestionModel(models.Model):
    total_marks = models.IntegerField(default=0)
    text = models.CharField(max_length=1000)
    lecture = models.ForeignKey(User,on_delete=models.CASCADE,blank=False,default=None,related_name='lecture')
    quiz = models.ForeignKey(Quiz,related_name='quiz',default=None, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.text

    def __str__(self): #for python3
        return self.text
  

class AnswerModel(models.Model):
    question        = models.ForeignKey(QestionModel,on_delete=models.CASCADE,default=None)
    answer_text     = models.CharField(max_length=100000,blank=True)
    is_correct      = models.BooleanField(default=False)
    student_user    = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True,default=None,related_name='student_user')

    def __str__(self):
        return f'key -  {self.question}'

    def __unicode__(self):
        return f'user responce to {self.question}'

