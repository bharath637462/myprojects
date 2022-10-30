from secapp.views import userviewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register('user', userviewset)