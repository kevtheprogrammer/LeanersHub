from django.contrib import admin

from .models import * 

admin.site.register([CourseCategoryModel,CourseModel,LessonModel,])