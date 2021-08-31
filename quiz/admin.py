from django.contrib import admin

from .models import Question, Choice, Tag

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 0

class TagInLine(admin.TabularInline):
    model = Tag
    extra = 0

class QuestionAdmin(admin.ModelAdmin):
    fields = ['text','pub_date','degree']
    inlines = [ChoiceInline, TagInLine]
    list_display = ('text', 'degree', 'pub_date')
    list_filter = ['pub_date', 'degree']
    search_fields = ['text']

admin.site.register(Question, QuestionAdmin)