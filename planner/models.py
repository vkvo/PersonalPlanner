from django.db import models


class Daily(models.Model):
    date = models.DateTimeField('Today')
    note = models.CharField(max_length=500)