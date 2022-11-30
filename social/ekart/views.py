from django.shortcuts import render
from ekart.models import Catagories,Products,Cart
from ekart.serializers import CategorySerializer,ProductSerializer,CartSerializer,ReviewSerializer,UserSerializer
from rest_framework.response import Response
from rest_framework import permissions,authentication
from rest_framework.viewsets import ModelViewSet,ViewSet
from rest_framework.decorators import action
# Create your views here.

#localhost:8000/user/signup/
class UsersignupView(ViewSet):
    def create(self,request,*args,**kwargs):
        serializer=UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


#localhost:8000/ekart/categories/
class CategoryView(ModelViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializer
    queryset = Catagories.objects.all()

##localhost:8000/ekart/categories/{id}/add_product
    @action(methods=["POST"],detail=True)
    def add_product(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cat=Catagories.objects.get(id=id)
        serilizer=ProductSerializer(data=request.data,context={"category":cat})
        if serilizer.is_valid():
            serilizer.save()
            return Response(data=serilizer.data)
        else:
            return Response(data=serilizer.errors)

#localhost:8000/ekart/catagories/{id}/get_products
    @action(methods=["GET"],detail=True)
    def get_products(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        cat=Catagories.objects.get(id=id)
        prdt=cat.products_set.all()
        serializer=ProductSerializer(prdt,many=True)
        return Response(data=serializer.data)

#localhost:8000/ekart/products/

class ProductView(ViewSet):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def list(self,request,*args,**kwargs):
        all_products=Products.objects.all()
        serilaizer=ProductSerializer(all_products,many=True)
        return Response(data=serilaizer.data)
 # localhost:8000/ekart/products/{id}

    def retrieve(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prdt=Products.objects.get(id=id)
        serializer=ProductSerializer(prdt,many=False)
        return Response(data=serializer.data)

# localhost:8000/ekart/products/{id}/add_cart
    @action(methods=["post"],detail=True)
    def add_cart(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prdt=Products.objects.get(id=id)
        user=request.user
        serializer=CartSerializer(data=request.data,context={"user":user,"product":prdt})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)

# localhost:8000/ekart/products/{id}/add_review
    @action(methods=["POST"],detail=True)
    def add_review(self,request,*args,**kwargs):
        id=kwargs.get("pk")
        prdt=Products.objects.get(id=id)
        user=request.user
        serializer=ReviewSerializer(data=request.data,context={"user":user,"product":prdt})
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data)
        else:
            return Response(data=serializer.errors)


class CartView(ModelViewSet):
    serializer_class = CartSerializer
    queryset = Cart.objects.all()
    permission_classes = [permissions.IsAuthenticated]
    def get_queryset(self):
        return Cart.objects.filter(user=self.request.user)



