from django.shortcuts import render
from django.views.generic import ListView , DetailView ,View

from .models import *


class CourserIndexView(ListView):

	model = CourseModel
	context_object_name = 'object_list'
	# paginate_by = 4

	def get_context_data(self,*args, **kwargs):
		context = super().get_context_data(**kwargs)
		cat = CourseCategoryModel.objects.all()
		context['course_category'] = cat
		return context


class CourserDetailView(DetailView):
	model = CourseModel
	context_object_name = 'object_list'

	def get_context_data(self,*args, **kwargs):
		context = super().get_context_data(**kwargs)
		obj_id = self.get_object().id
		cat = LessonModel.objects.filter(course__id = obj_id)
		context['lessons'] = cat
		return context

class CourserLessonDetailView(DetailView):
	model = LessonModel
	context_object_name = 'object_list'