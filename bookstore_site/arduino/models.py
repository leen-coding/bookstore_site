from django.db import models


# Create your models here.
class IoT(models.Model):
    prime = models.IntegerField(primary_key=True,null=False,unique=True,default=0)
    temperature = models.DecimalField(max_digits=5, decimal_places=2)
    humidity = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "IoT"