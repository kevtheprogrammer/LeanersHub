from django.db import models
from assessments.models import Quiz

# Create your models here.
from courses.models import *


class CourseOutlineModel(models.Model):
    course = models.ForeignKey( CourseModel,on_delete=models.CASCADE,default=None,related_name="course_name" )
    title = models.CharField(max_length=120)
    description = models.TextField(help_text='*learning objectives*')
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)

    

    def __str__(self):
        return f'{self.course} {self.title}'

    def __unicode__(self):
        return f'{self.title}'

class LessonWeekModel(models.Model):
    index = models.IntegerField(default=1)
    lesson = models.ForeignKey(LessonModel,on_delete=models.CASCADE,default=None,blank=False,related_name='courser_outline')
    test = models.ManyToManyField(Quiz,default=None,related_name='tester',blank=True)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    updated = models.DateField(auto_now=True, auto_now_add=False)

    
    def __str__(self):
        return f'Lesson {self.index} - {self.lesson.course}'

 