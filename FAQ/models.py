from django.db import models


class Qna(models.Model):
        title = models.CharField(max_length=50)
        text = models.TextField()