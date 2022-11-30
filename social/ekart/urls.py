from django.urls import path
from ekart import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register("user/signup",views.UsersignupView,basename="user"),
router.register("categories",views.CategoryView,basename="cat"),
router.register("products",views.ProductView,basename="prdt"),
router.register("carts",views.CartView,basename="cart")




urlpatterns=[


]+router.urls