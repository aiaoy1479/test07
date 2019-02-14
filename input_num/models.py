from django.db import models

class Total_input(models.Model):
    num = models.CharField(max_length=20)
    total = models.IntegerField()

    def __str__(self):
        return self.num

