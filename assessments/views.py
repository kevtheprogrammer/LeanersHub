from django.shortcuts import render
from django.views.generic import ListView , DetailView ,View

from .forms import QuestionForm

from .models import *

class CourserTestDetailView(DetailView):
	model = Quiz
	form_class  = QuestionForm
	context_object_name = 'object_list'

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		obj_id = self.get_object().id
		context["questions"] = QestionModel.objects.filter(quiz__id = obj_id)
		return context
	
	def post(self,request, *args, **kwargs):
		obj_id = self.get_object().id
		que = QestionModel.objects.filter(quiz__id = obj_id)
		for question in que:
			selected_answer = request.POST.get(str(question.id))
			if selected_answer:
				answer = AnswerModel.objects.get(id=selected_answer)
       			
          		# if answer.is_correct:
      			# 	pass
					#score += 1
     
					
     
  
  
  