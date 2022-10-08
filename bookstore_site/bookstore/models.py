from django.db import models


# Create your models here.
class books(models.Model):
    title = models.CharField(max_length=50, default='')
    publisher = models.CharField(max_length=50, default='')
    price = models.IntegerField(default=0)
    market_price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        db_table = "books"


# books.objects.create(title="Python3", publisher="机械工业出版社", price=15, market_price=20.55)
# books.objects.create(title="Mysql", publisher="北京大学出版社", price=10, market_price=25.22)
# books.objects.create(title="如何养鱼", publisher="大连理工大学出版社", price=20, market_price=35.20)
# books.objects.create(title="机械设计制造", publisher="机械工业出版社", price=35, market_price=39.99)
