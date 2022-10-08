from django.db import models


# Create your models here.
class book(models.Model):
    title = models.CharField('书名', max_length=50, default='')
    price = models.DecimalField(max_digits=7, decimal_places=2, default='')
    info = models.CharField('信息', max_length=50, default='')
    date = models.DateTimeField(auto_now=True)
    score = models.FloatField()
    int = models.IntegerField(default='0')
    # email = models.EmailField('email')
    textfiel = models.TextField()
    int2 = models.IntegerField(null=True)
    int3 = models.IntegerField(default=0)
    class Meta:
            db_table = 'book'

class card(models.Model):
    title = models.CharField(max_length=50,default='')
    price = models.IntegerField(default=0)
    class Meta:
        db_table = 'card'