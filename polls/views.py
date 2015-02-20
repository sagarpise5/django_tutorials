from django.http import HttpResponse
from django.shortcuts import render

from polls.models import Question


def index(request):
    # latest_question_list = Question.objects.order_by( '-pub_date' )[ :5 ]
    # template = loader.get_template( 'polls/index.html' )
    # context = RequestContext( request, { 'latest_question_list' : latest_question_list } )
    # print("context : ", context)
    # return HttpResponse( template.render(context ))

    latest_three_questions = Question.objects.order_by('-pub_date')[:5                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          ]
    ctx = {'latest_question_list': latest_three_questions}
    return render(request, 'polls/index.html', ctx)


def details(request, question_id):
    # print("details method : request --", request, '\tquestion_id--', question_id)
    return HttpResponse('You are looking at question %s,' % question_id)


def results(request, question_id):
    # print("results method : request --", request, '\tquestion_id--', question_id)
    result = 'You are looking for answer of question %s'
    print("result  : ", result)
    return HttpResponse(result % question_id)


def vote(request, question_id):
    # print("vote method : request --", request, '\tquestion_id--', question_id)
    return HttpResponse('You are Voting on question %s' % question_id)
