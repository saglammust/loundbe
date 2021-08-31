from django.contrib import admin

from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fields = ['text','pub_date','degree']
    inlines = [ChoiceInline]
    list_display = ('text', 'degree', 'subject', 'pub_date')
    list_filter = ['pub_date', 'degree', 'subject']
    search_fields = ['text', 'subject']

admin.site.register(Question, QuestionAdmin)