from django.db import models

# Create your models here.
class Events(models.Model):
    name = models.CharField(max_length=255,null=True,blank=True)
    start = models.DateTimeField(null=True,blank=True)
    end = models.DateTimeField(null=True,blank=True)

    class Meta:
        db_table = "tblevents"