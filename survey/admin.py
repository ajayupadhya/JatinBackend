from django.contrib import admin

# Register your models here.

from .models import (SurveyAnswerModal , SurveyQuestionModal , SinglePage , Client)



admin.site.register(SurveyAnswerModal)
admin.site.register(SurveyQuestionModal)
admin.site.register(Client)
admin.site.register(SinglePage)