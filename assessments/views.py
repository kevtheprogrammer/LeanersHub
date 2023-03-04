from django.shortcuts import render,redirect
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
		obj = self.get_object()
		user = request.user
		que = QestionModel.objects.filter(quiz__id = obj_id)
		
		score = 0
		for question in que:
			point = question.total_marks
			selected_answer = request.POST.get(str(question.id))
			if selected_answer:
				answer = AnswerModel.objects.get(id=selected_answer)
				if answer.is_correct:
					print(score,point)
					score += point
					score_object = ScoreModel.objects.create_score(user,obj,score)
					score_object.save()
					item = score_object.id
		return redirect('assessment:score',pk=item)

class ScoreModelDetailView(DetailView):
	model = ScoreModel
	context_object_name = 'object_list'
		
     


  
  