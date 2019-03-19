from django.db import models
from django.shortcuts import reverse
from froala_editor.fields import FroalaField
from django.utils import timezone

class Bulletinboard(models.Model):
        writer = models.CharField(max_length=15)
        title = models.CharField(max_length=200)
        text = FroalaField(theme='dark')
        created_date = models.DateTimeField(
                default=timezone.now)
        published_date = models.DateTimeField( 
                blank=True, null=True)
        secret = models.BooleanField()
        password = models.CharField(max_length=20)
        

        def publish(self):
                self.published_date = timezone.now()
                self.save()

        def __str__(self):
                return self.title
        
        def get_absolute_url(self):
                return reverse('bulletinboard:board_detail', args=[self.pk])

class Comment(models.Model):
        writer = models.CharField(max_length=15)
        text = FroalaField(theme='dark')
        created_date = models.DateTimeField(default=timezone.now)
        post = models.ForeignKey(Bulletinboard, null=True, blank=True, on_delete=models.CASCADE)
        id = models.AutoField(primary_key=True)
