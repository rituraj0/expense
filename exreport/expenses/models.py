from django.db import models

# Create your models here.
class Expense(models.Model):
    Name = models.CharField(max_length=200)
    Cost = models.FloatField(default=1000000)

    def __unicode__(self):
        return self.Name
