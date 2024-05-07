from django.db import models

DIFF_CHOICES=(
    ('easy','easy'),
    ('medium','medium'),
    ('difficult','difficult')
)


class Quiz(models.Model):
    name= models.CharField(max_length=225)
    topic = models.CharField(max_length=120)
    number_of_questions = models.IntegerField() 
    time = models.IntegerField(help_text="duration of the quiz")
    required_score_to_pass = models.IntegerField(help_text="required_score_to_pass")
    difficulty = models.CharField(max_length=10,choices=DIFF_CHOICES)
    
    def __str__(self):
        return self.name
    
    def get_questions(self):
        return self.question_set.all()