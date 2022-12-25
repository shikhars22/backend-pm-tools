from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=1300)
    img = models.CharField(max_length=1300)