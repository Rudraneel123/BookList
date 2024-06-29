from django.db import models


class Bookbuy(models.Model):
    id=models.IntegerField(primary_key=True)
    title=models.CharField(max_length=250)
    author=models.CharField(max_length=250)
    price=models.DecimalField(max_digits=5,decimal_places=2)
    
    class Meta:
       managed=False
       db_table='book_buy'
        
        