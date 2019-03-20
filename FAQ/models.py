from django.db import models
from froala_editor.fields import FroalaField

class Qna(models.Model):
        title = models.CharField(max_length=50)
        text = models.TextField()