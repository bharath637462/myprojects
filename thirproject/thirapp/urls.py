from django.urls import path

from thirapp.views import UserViewset, CategoryViewset, MaterialViewset, OrderViewset, UserReviewViewset
from rest_framework import routers


urlpatterns = [
    path('materials_views', MaterialViewset.materials_reviews),
]
router = routers.DefaultRouter()
router.register('users', UserViewset)
router.register('categories', CategoryViewset)
router.register('materials', MaterialViewset)
router.register('orders', OrderViewset)
router.register('reviews', UserReviewViewset)

