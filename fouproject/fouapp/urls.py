from fouapp.views import Userviewset, Categoryviewset, Materialviewset, Orderviewset, UserReviewviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('users', Userviewset)
router.register('categories', Categoryviewset)
router.register('materials', Materialviewset)
router.register('orders', Orderviewset)
router.register('reviews', UserReviewviewset)