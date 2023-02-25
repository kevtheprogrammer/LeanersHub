# from django.db import models
# from __future__ import unicode_literals
# from django.core.urlresolvers import reverse


# # Create your models here.
# class CourseModel(models.Model):
#     title = models.CharField(max_length=120)
#     description = models.TextField()
#     cost = models.CharField(max_length=120)
#     duration = models.CharField(max_length=120)
#     category= models.CharField(max_length=120)
#     modeOfDelivery = models.CharField(max_length=120)
#     skillLevel = models.CharField(max_length=120)
#     prerequisite = models.CharField(max_length=120)
#     updated = models.DateField(auto_now=True, auto_now_add=False)
#     timestamp = models.DateField(auto_now=False, auto_now_add=True)

#     def __unicode__(self):
#         return self.title

#     def __str__(self): #for python3
#         return self.title

#     # def get_absolute_url(self):
#     #     return reverse("s:retrieve", kwargs={"id": self.id})