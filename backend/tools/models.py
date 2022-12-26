from django.db import models

class Tool(models.Model):
    name = models.CharField(max_length=300)
    desc = models.CharField(max_length=1300)
    longDesc = models.CharField(max_length=2300, default='')
    img = models.CharField(max_length=1300)
    isActive = models.BooleanField(default=True)