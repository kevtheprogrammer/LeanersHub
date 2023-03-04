from django.forms import ModelForm
 
from .models import *

class AnswerForm(ModelForm):
    class Meta:
        model = AnswerModel
        fields = ('answer_text',)

class QuestionForm(ModelForm):
    class Meta:
        model = QestionModel
        fields = [ 'text',]