from .models import Quiz
from django import forms
class QuizForm(forms.Form):
    # ques = forms.CharField(max_length= 100, label = 'enter the question')
    # choice1= forms.CharField(max_length= 100, label = 'enter the choice1')
    # choice2 = forms.CharField(max_length=100, label='enter the choice1')
    class Meta:
        model = Quiz
        fields = '__all__'