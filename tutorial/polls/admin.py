from django.contrib import admin
from .models import Question

# Register your models here.

# Provides a pre-build/scafold from Question Model
# admin.site.register(Question)

# Provides a custom Question Model
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(Question, QuestionAdmin)