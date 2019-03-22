from django.db import models
from froala_editor.fields import FroalaField

class FAQ(models.Model):
        question = models.CharField(max_length=50)
        answer = FroalaField()