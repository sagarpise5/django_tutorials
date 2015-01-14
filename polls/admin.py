from django.contrib import admin

from polls.models import Question, Choice


class ChoiceInline( admin.TabularInline ) :
    model = Choice
    extra = 1


class QuestionAdmin( admin.ModelAdmin ) :
    # fields = ['pub_date', 'question_text']
    fieldsets = [ ('Question', { 'fields' : [ 'question_text' ] }),
                  ('Date information', { 'fields' : [ 'pub_date' ] }),
                  ('Date information', { 'fields' : [ 'pub_date' ], 'classes' : ('collapse',) }), ]
    list_display = ('question_text', 'pub_date', 'was_published_recently', )
    list_display_links = ('question_text', 'pub_date')
    # list_editable = ['pub_date']
    list_filter = ('pub_date', 'question_text',)
    inlines = [ ChoiceInline ]
    list_per_page = 5
    list_max_show_all = 10
    # save_on_top = True
    search_fields = [ 'pub_date' ]


admin.site.register( Question, QuestionAdmin )
# admin.site.register(Choice)
