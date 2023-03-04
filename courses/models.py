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
    slug   = models.SlugField( default=None )

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
    slug   = models.SlugField( default=None )
    # bookmarked = models.ManyToMany(User)
    # completed = models.ManyToManyField(User)
    # course_code = models.CharField(max_length=120)
    
    def snippet(self):
        return f'{self.description[:100]}...'

    def __unicode__(self):
        return self.title

    def __str__(self): #for python3
        return self.title

    def get_absolute_url(self):
        return reverse("courses:couse-outline", kwargs={"slug": self.slug})
    
class LessonModel(models.Model):
    # module_code = models.CharField(max_length=120)
    # bookmarked = models.ManyToMany(User)
    # completed = models.ManyToManyField(User)
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
    slug   = models.SlugField( default=None )

    def __unicode__(self):
        return f'{self.title} - {self.course}'

    def __str__(self): #for python3
        return f'{self.title} - {self.course}'
    
    def get_absolute_url(self):
        return reverse("courses:lesson", kwargs={"slug1": self.course.slug,"slug": self.slug})
    
    def snippet(self):
        return f'{self.description[:100]}...'
    
class PackModel(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(help_text='*Benefits*')
    price = models.DecimalField(decimal_places=2,max_digits=20,default=0.00)
    discount = models.DecimalField(decimal_places=2,max_digits=20,default=0.00)
    expires = models.CharField(max_length=1000,help_text='1 month')
    is_published = models.BooleanField(default=False) 
    _course = models.ManyToManyField( CourseModel,related_name="_course" )
    slug   = models.SlugField( default=None )
    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
    writer = models.ForeignKey( User,on_delete=models.CASCADE,default=None,related_name="writer" )
    
    def __str__(self):
        return f'{self.title}'

class UserSubscriptionPackModel(models.Model):
    student = models.ForeignKey( User,on_delete=models.CASCADE,default=None,related_name="student" )
    pack =  models.ForeignKey( PackModel,on_delete=models.CASCADE,default=None,related_name="pack" )
    updated = models.DateField(auto_now=True, auto_now_add=False)
    timestamp = models.DateField(auto_now=False, auto_now_add=True)
   

    def __str__(self):
        return f'{self.pk} - {self.student.first_name} subscription for {self.pack.title}'

    def __unicode__(self):
        return f'{self.pk} - {self.student.first_name} subscription for {self.pack.title}'

