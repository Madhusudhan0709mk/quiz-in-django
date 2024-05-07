from django.shortcuts import render,HttpResponse
from .models import Quiz

def home(request):
    # quiz = Quiz.objects.get(pk=quiz_id)
    # return render(request, 'quiz_detail.html', {'quiz': quiz})
    return HttpResponse("hi")