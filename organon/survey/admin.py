from django.contrib import admin
from survey.models import Question,Options,Response
# Register your models here.
class QuestionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Question._meta.get_fields()]

admin.register(Question,QuestionsAdmin)

class OptionsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Options._meta.get_fields()]
admin.register(Options,OptionsAdmin)

class ResponseAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Response._meta.get_fields()]
admin.register(Response,ResponseAdmin)