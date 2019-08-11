from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from .models import Question, Choice


def index(request):
    latest_questions = Question.objects.order_by(
        '-id'
    )[:5]
    return render(
        request,
        'polls/index.html',
        {'latest_questions_list': latest_questions}
    )


def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(
        request,
        'polls/detail.html',
        context={'question': question}
    )

def results(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    return render(
        request,
        'polls/results.html',
        context={'question': question}
    )

def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        selected_choice = question.choice_set.get(
            id=request.POST['choice']
        )
    except Choice.DoesNotExist:
        return render(
            request,
            'polls/detail.html',
            {
                'question': question,
                'error_message': "You didn't select a choice"
            }
        )
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(
            reverse('polls:results', args=[question.id])
        )
    return HttpResponse(
        request.POST
    )
