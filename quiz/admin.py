from django.contrib import admin
from .models import Choice,Question,Quiz,UserQuizAttempt,Account,UserProfile
# Register your models here.

#Admin can add the choices right after one another
class ChoiceInline(admin.TabularInline):
  model=Choice
  extra=1

#Choice Table gets built inside Question model of Admin Interface
class QuestionAdmin(admin.ModelAdmin):
  list_display = ('question', 'created_at')
  inlines = [ChoiceInline] 

#Registering all models so that Admin can manipulate the data
admin.site.register(Account)
admin.site.register(Quiz)
admin.site.register(Question,QuestionAdmin)
admin.site.register(UserQuizAttempt)
admin.site.register(UserProfile)


