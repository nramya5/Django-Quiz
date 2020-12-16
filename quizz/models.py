from django.db import models

# Create your models here.
class Question(models.Model):
    ques = models.CharField(max_length= 100)
    choice1 = models.CharField(max_length=100, unique= True)
    choice2 = models.CharField(max_length=100, unique= True)
    choice3 = models.CharField(max_length=100, unique=True)
    choice4 = models.CharField(max_length=100, unique= True)
    correct_ans= models.CharField(max_length=100, unique= True)
    quiz_no = models.CharField(max_length= 100)
    def __str__(self):
        return self.ques



class Answer(models.Model):
    question= models.ForeignKey(Question, on_delete= models.CASCADE)
    text = models.CharField(max_length= 100)
    is_correct = models.BooleanField(default= False)
    quiz_no = models.CharField(max_length=100)
    def __str__(self):
        return self.text

class Quiz(models.Model):
    quiz_no= models.CharField(max_length= 100)
    question_counts= models.IntegerField()
    created= models.DateTimeField(auto_now_add=True, null= True, blank=True)
    user = models.CharField(max_length= 1000)


