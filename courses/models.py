from __future__ import unicode_literals
from django.db import models
from django.urls import reverse


from acc.models import User

class CourseCategoryModel(models.Model):
    coverImg = models.ImageField(upload_to='course_categrogy/')
    title = models.CharField(max_length=120)
    description = models.TextField()
    maker = models.ForeignKey( User,on_delete=models.CASCADE,default=None,related_name="maker" )
    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)

    def __unicode__(self):
        return self.title

    def __str__(self): #for python3
        return self.title


class CourseModel(models.Model):
    coverImg = models.ImageField(upload_to='courses/')
    title = models.CharField(max_length=120)
    description = models.TextField()
    cost = models.CharField(max_length=120)
    duration = models.CharField(max_length=120)
    category = models.ForeignKey( CourseCategoryModel,on_delete=models.CASCADE,default=None,related_name="category" )
    skillLevel = models.CharField(max_length=120)
    requirements = models.CharField(max_length=120)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    creator = models.ForeignKey( User,on_delete=models.CASCADE,default=None,related_name="creator" )

    def __unicode__(self):
        return self.title

    def __str__(self): #for python3
        return self.title

    # def get_absolute_url(self):
    #     return reverse("s:retrieve", kwargs={"id": self.id})
    
    
class LessonModel(models.Model):
    coverImg = models.ImageField(upload_to='courses/')
    title = models.CharField(max_length=120)
    description = models.TextField(help_text='*learning objectives*')
    progress = models.IntegerField(verbose_name="progress level")
    bookmark = models.BooleanField(verbose_name="Bookmark",default=False)
    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    video_link = models.TextField( default=None,verbose_name="video link" , blank = True )
    main_content = models.TextField(help_text='*learning objectives*')
    is_published = models.BooleanField(default=False) 
    course = models.ForeignKey( CourseModel,on_delete=models.CASCADE,default=None,related_name="course" )
    author = models.ForeignKey( User,on_delete=models.CASCADE,default=None,related_name="author" )

    def __unicode__(self):
        return self.title

    def __str__(self): #for python3
        return self.title
