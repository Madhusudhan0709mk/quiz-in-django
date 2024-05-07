from django.db import models
from quiz.models import *
# Create your models here.
class Question(models.Model):
    text= models.CharField(max_length=225)
    quiz= models.ForeignKey(Quiz,on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.text)
    
    def get_answers(self):
        return self.answer_set.all()
    
class Answer(models.Model):
    text= models.CharField(max_length=225)
    
    question= models.ForeignKey(Question,on_delete=models.CASCADE,related_name='questions')
    
    correct = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f" question:{self.question.text},answer:{self.text}"