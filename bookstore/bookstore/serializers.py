from .models import Bookbuy
from rest_framework import serializers


class BookListSerializers(serializers.ModelSerializer):
    class Meta:
        model=Bookbuy
        fields=['id','title','author','price']
        
   