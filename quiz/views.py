from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse, Http404

from .models import Question

def index(request):
    latest_question_list = Question.objects.order_by('-tarih')[:5]
    context = {'latest_question_list': latest_question_list,}
    return render(request, 'quiz/index.html', context)

def detail(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Bu soru veritabanında bulunmamaktadır.")
    return render(request, 'quiz/detail.html', {'question': question})

def results(request, question_id):
    response = "%s. sorunun doğru cevabını görmektesiniz."
    return HttpResponse(response % question_id)

def answer(request, question_id):
    return HttpResponse("%s. soruyu cevaplandırıyorsunuz." % question_id)
