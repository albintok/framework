from rest_framework import serializers
from bikes.models import Vechicles

class BikeSerializers(serializers.Serializer):
    id=serializers.CharField(read_only=True)
    name=serializers.CharField(max_length=20)
    colour=serializers.CharField(max_length=20)
    cc=serializers.IntegerField()
    price=serializers.IntegerField()
    brand=serializers.CharField(max_length=20)


#modelSerializer:-

class BikeModelSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Vechicles
        fields="__all__"
        #or fields=["name","colour","cc","price","brand"]