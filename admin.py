from django.contrib import admin
from .models import *

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 6  # Show 6 answer fields by default (one for each representational system)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ['question', 'category']
    search_fields = ['question']
    list_filter = ['category']

class AnswerAdmin(admin.ModelAdmin):
    list_display = ['answer', 'question', 'rep_system']
    search_fields = ['answer', 'question__question']
    list_filter = ['rep_system']

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['category_name']
    search_fields = ['category_name']

class QuizResultAdmin(admin.ModelAdmin):
    list_display = ['uid', 'created_at', 'get_dominant_system']
    readonly_fields = ['visual_count', 'auditory_count', 'kinesthetic_count', 
                       'olfactory_count', 'gustatory_count', 'auditory_digital_count']

# Register models
admin.site.register(Category, CategoryAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
admin.site.register(QuizResult, QuizResultAdmin)
