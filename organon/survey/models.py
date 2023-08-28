from django.db import models

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    correct_option = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    class Meta:
        app_label="survey"

class Options(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    option = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.option
    class Meta:
        app_label="survey"

class Response(models.Model):
    question = models.ForeignKey(to=Question, on_delete=models.CASCADE)
    option = models.ForeignKey(to=Options, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        app_label="survey"