from django.contrib import admin
from .models import Choice, Question

# Register your models here.

# Provides a pre-build/scafold from Question Model
# admin.site.register(Question)

# class ChoiceInline(admin.StackedInline): like a stack
# Like a table
class ChoiceInline(admin.TabularInline):
    # The model to show in a inline view
    model = Choice

    # Number of inline choices to show
    extra = 3

# Provides a custom Question Model
class QuestionAdmin(admin.ModelAdmin):
    # Set of data to show and how to show
    fieldsets = [
        (None,  {'fields' : ['question_text']}),
        ('Date information', {'fields':['pub_date'], 'classes':['collapse']}),
    ]

    # Selection in an inline view
    inlines = [ChoiceInline]

    # Display of data to show about Question
    list_display = ('question_text', 'pub_date', 'was_published_recently')

    # Adding filter to the view
    list_filter = ['pub_date']

    # Search capability
    search_fields = ['question_text']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice)