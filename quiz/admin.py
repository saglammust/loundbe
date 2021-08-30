from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4


class QuestionAdmin(admin.ModelAdmin):
    fields = ['text','pub_date']
    inlines = [ChoiceInline]
    list_display = ('text', 'degree', 'pub_date')
    list_filter = ['pub_date', 'degree']
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)