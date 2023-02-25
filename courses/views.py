from django.shortcuts import render
from django.views.generic import ListView , DetailView ,View

from .models import *


class CourserIndexScreen(ListView):

	model = CourseModel
	paginate_by = 4
	context_object_name = 'object_list'

	def get_context_data(self,*args, **kwargs):
		context = super().get_context_data(**kwargs)
		cat = CourseCategoryModel.objects.all()
		context['course_category'] = cat
		return context
