from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import Question


def index(request):
  latest_question_list: list[Question] = Question.objects.order_by('-publish_datetime')[:5]
  context = { latest_question_list }
  
  return render(request, 'polls/index.html', context)


def detail(request, question_id):
  question = get_object_or_404(
    Question,
    pk=question_id
  )
  
  return render(
    request,
    'polls/detail.html',
    {
      'question': question
    }
  )


def results(request, question_id):
  response: str = 'You are looking at the result of question %s.'
  return HttpResponse(response % question_id) 


def vote(request, question_id):
  return HttpResponse('You are voting on question %s.'% question_id) 