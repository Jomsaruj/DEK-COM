from django.db import models

class IdCode(models.Model):
    code = models.CharField(max_length=6, default='')

