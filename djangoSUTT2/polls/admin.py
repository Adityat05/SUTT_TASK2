from django.contrib import admin

from .models import Choice, Question

#ChoiceInline is an inline model that allows choice cobejcts to be edited inside the question admin page
class ChoiceInline(admin.TabularInline):#stackedinline means choice appear in stack
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ("text of the question", {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"], "classes": ["collapse"]}),
    ]
    inlines = [ChoiceInline]
    list_display = ["question_text", "pub_date", "was_published_recently"]
    list_filter = ["pub_date"]
    search_fields = ["question_text"]


admin.site.register(Question, QuestionAdmin)