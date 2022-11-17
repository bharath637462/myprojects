from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from . import serializer, custompermissions
from .ViewSetActionPermissionMixin import ViewSetActionPermissionMixin
from .models import Category, Material, User, Order, UserReview
from rest_framework.response import Response


class UserViewset(ViewSetActionPermissionMixin, viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer
    permission_action_classes = {
        'create': (custompermissions.IsManager | custompermissions.IsUser,),
        'list': (custompermissions.IsManager,),
        'retrieve': (custompermissions.IsAdmin | custompermissions.IsManager,),
        'update': (custompermissions.IsAdmin | custompermissions.IsManager,),
    }

    @action(detail=True, url_name='orders', url_path='orders')
    def orders(self, request, pk):
        print(self.get_object().orders.all())
        return Response([{'order_id': order.id, 'material': material.name, 'category': material.category.name} for order in self.get_object().orders.all() for material in order.materials.all()])


class CategoryViewset(ViewSetActionPermissionMixin, viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = serializer.CategorySerializer
    permission_action_classes = {
        'create': (custompermissions.IsAdmin | custompermissions.IsManager,),
        'list': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
        'retrieve': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
        'update': (custompermissions.IsAdmin | custompermissions.IsManager,),
    }


class MaterialViewset(ViewSetActionPermissionMixin, viewsets.ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = serializer.MaterialSerializer
    permission_action_classes = {
        'create': (custompermissions.IsManager | custompermissions.IsAdmin | custompermissions.IsUser,),
        'list': (custompermissions.IsAdmin | custompermissions.IsUser | custompermissions.IsManager,),
        'retrieve': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
        'update': (custompermissions.IsAdmin | custompermissions.IsManager,),
        'delete': (custompermissions.IsAdmin,)
    }

    @action(detail=True, url_name='reviews', url_path="reviews")
    def materials_reviews(self, request, pk):
        return Response([{'user': re.user.first_name, 'review': re.review} for re in self.get_object().reviews.all()])


class OrderViewset(ViewSetActionPermissionMixin, viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializer.OrderSerializer
    permission_action_classes = {
        'create': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
        'list': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
        'retrieve': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
        'update': (custompermissions.IsUser,),
    }


class UserReviewViewset(ViewSetActionPermissionMixin, viewsets.ModelViewSet):
    queryset = UserReview.objects.all()
    serializer_class = serializer.UserReviewSerializer
    permission_action_classes = {
        'create': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
        'list': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
        'retrieve': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
        'update': (custompermissions.IsAdmin | custompermissions.IsManager | custompermissions.IsUser,),
    }
