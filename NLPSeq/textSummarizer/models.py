from django.db import models

# Create your models here.

class Text(models.Model):
    input_text = models.TextField()
    summary = models.TextField()
    time_taken = models.FloatField(default=0.0)

