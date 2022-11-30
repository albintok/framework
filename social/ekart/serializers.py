from ekart.models import User,Catagories,Products,Cart,Review
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["first_name","last_name","username","password"]
    def create(self,validated_data):
        return User.objects.create_user(**validated_data)


class CategorySerializer(serializers.ModelSerializer):
    is_active=serializers.BooleanField(read_only=True)
    id=serializers.CharField(read_only=True)
    class Meta:
        model=Catagories
        fields=["catagory_name","is_active","id"]


class ProductSerializer(serializers.ModelSerializer):
    id=serializers.CharField(read_only=True)
    catagory=serializers.CharField(read_only=True)
    class Meta:
        model=Products
        fields="__all__"
    def validate_price(self,value):
        if value not in range(50,50000):
            raise serializers.ValidationError("invalid_price")
        return value
    def create(self, validated_data):
        catagory=self.context.get("category")
        return Products.objects.create(**validated_data,catagory=catagory)

class CartSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=ProductSerializer()
    created_date=serializers.CharField(read_only=True)
    status=serializers.CharField(read_only=True)
    class Meta:
        model=Cart
        fields='__all__'
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Cart.objects.create(**validated_data,user=user,product=product)

class ReviewSerializer(serializers.ModelSerializer):
    user=serializers.CharField(read_only=True)
    product=serializers.CharField(read_only=True)
    class Meta:
        model=Review
        fields="__all__"
    def create(self, validated_data):
        user=self.context.get("user")
        product=self.context.get("product")
        return Review.objects.create(**validated_data,user=user,product=product)