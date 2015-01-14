__author__ = 'sagar'
from django.conf.urls import url, patterns

from polls import views


urlpatterns = patterns( '',
                        # ex: /polls/
                        url( r'^$', views.index, name = 'index' ),
                        # ex: /polls/5/
                        url( r'^(?P<question_id>\d+)/$', views.details, name = 'detail' ),
                        # ex: /polls/5/results/
                        url( r'^(?P<question_id>\d+)/results/$', views.results, name = 'results' ),
                        # ex: /polls/5/vote/
                        url( r'^(?P<question_id>\d+)/vote/$', views.vote, name = 'vote' ),
)
