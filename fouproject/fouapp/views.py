# from django.contrib.auth.decorators import login_required
# from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType

# from django.contrib.contenttypes.models import ContentType
# from django.http import HttpResponse
from rest_framework import viewsets
# >>> from authentication.models import User
# >>> user = User.objects.get(username='johnsmith')
# >>> from django.contrib.auth.models import Permission
# >>> permission = Permission.objects.get(codename='add_photo')
# >>> user.user_permissions.add(permission)

from . import serializer
# from .mixin import GroupRequiredMixin
from .models import Category, Material, User, Order, UserReview


# manager_group, created = Group.objects.get_or_create(name="Manager")
#
# perms = ['Can add material',
#                        # 'Can change material', 'Can delete material', 'Can view material'
#                        # 'Can add category', 'Can change category', 'Can delete category', 'Can view category'
#                        ]
# for perm in perms:
#     proj_add_perm = Permission.objects.get(name=perm)
#     manager_group.permissions.add(proj_add_perm)


# user_group, created = Group.objects.get_or_create(name="User")
# permissions = ['Can add material', 'Can view category']
# for permission in permissions:
#     proj_add_perm = Permission.objects.get(name=permission)
#     user_group.permissions.add(proj_add_perm)

#
# @login_required
# def addtoManager(request):
#     user_group, created = Group.objects.get_or_create(name="manager")
#     ct = ContentType.objects.get_for_model(User)
#     perms = (
#         {"name": "Can add material", "codename": "add_material", "content_type": ct},
#         {"name": "Can delete material", "codename": "delete_material", "content_type": ct},

        # 'Can change material'
        # 'Can delete material',
        # 'Can view material'
        # 'Can add category',
        # 'Can change category',
        # 'Can delete category',
        # 'Can view category'
    # )
    #
    # for perm in perms:
    #     # import pdb; pdb.set_trace()
    #     # Permission.objects.all()
    #     proj_add_perm, created = Permission.objects.get_or_create(name=perm["name"], codename=perm["codename"],
    #                                                               content_type=perm["content_type"])
    #     user_group.permissions.add(proj_add_perm)
    # return HttpResponse(request.user.objects)
    #

# @login_required
# def addtoUser(request):
#     user_group, created = Group.objects.get_or_create(name="user")
#     ct = ContentType.objects.get_for_model(User)
#     perms = (
#         {"name": "Can add material", "codename": "add_material", "content_type": ct},
#         # {"name": "Can delete material", "codename": "delete_material", "content_type": ct},
#
#         # 'Can change material'
#         # 'Can delete material',
#         # 'Can view material'
#         # 'Can add category',
#         # 'Can change category',
#         # 'Can delete category',
#         # 'Can view category'
#     )

    # for perm in perms:
    #     # import pdb; pdb.set_trace()
    #     # Permission.objects.all()
    #     proj_add_perm, created = Permission.objects.get_or_create(name=perm["name"], codename=perm["codename"],
    #                                                               content_type=perm["content_type"])
    #     user_group.permissions.add(proj_add_perm)
    # return HttpResponse("hi hello")


# user = User.objects.get(username=request.user.email)
# user.groups.add(manager_group)
# return HttpResponse(request.user.groups)


#     # user = request.user
#     # user.groups.add(new_group)
#     return HttpResponse("hi")

# ct = ContentType.objects.get_for_model(request.user)
# Permissions = ('thirapp.add_material', 'thirapp.change_material',  'thirapp.delete_material')
# for permission in Permissions:
#     # permissions = Permission.objects.create(permission)
#     # new_group.permissions.add(permissions)
#     return HttpResponse(permission)


# User.groups.add(user_group)
class Userviewset(viewsets.ModelViewSet):
    # permission_required = ('thirapp.add_user', 'thirapp.change_user', 'thirapp.delete_user', 'thirapp.view_user')
    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer


class Categoryviewset(viewsets.ModelViewSet):
    # permission_required = (
    #     'thirapp.add_category', 'thirapp.change_category', 'thirapp.delete_category', 'thirapp.view_category')
    queryset = Category.objects.all()
    serializer_class = serializer.CategorySerializer


class Materialviewset( viewsets.ModelViewSet):
    group_required = [u'manager']

    # permission_required = (
    #     'thirapp.add_material', 'thirapp.change_material', 'thirapp.delete_material', 'thirapp.view_material')
    queryset = Material.objects.all()
    serializer_class = serializer.MaterialSerializer



class Orderviewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializer.OrderSerializer


class UserReviewviewset(viewsets.ModelViewSet):
    queryset = UserReview.objects.all()
    serializer_class = serializer.UserReviewSerializer
