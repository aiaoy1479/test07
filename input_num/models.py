from django.db import models

class Number(models.Model):
    num_input = models.CharField(max_length=20)

class Total_input(models.Model):
    num = models.ForeignKey(Number, on_delete=models.CASCADE)
    total = models.IntegerField()

