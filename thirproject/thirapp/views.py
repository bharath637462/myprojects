from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from rest_framework import viewsets
from . import serializer
from .mixin import GroupRequiredMixin
from .models import Category, Material, User, Order, UserReview


@login_required
def addtoManager(request):
    user_group, created = Group.objects.get_or_create(name="manager")
    ct = ContentType.objects.get_for_model(User)
    perms = (
        {"name": "Can add material", "codename": "add_material", "content_type": ct},
        {"name": "Can delete material", "codename": "delete_material", "content_type": ct},

        'Can change material'
        'Can delete material',
        'Can view material'
        'Can add category',
        'Can change category',
        'Can delete category',
        'Can view category'
    )

    for perm in perms:
        # import pdb; pdb.set_trace()
        # Permission.objects.all()
        proj_add_perm, created = Permission.objects.get_or_create(name=perm["name"], codename=perm["codename"],
                                                                  content_type=perm["content_type"])
        user_group.permissions.add(proj_add_perm)
    return HttpResponse("ypu are now manager")


#

@login_required
def addtoUser(request):
    user_group, created = Group.objects.get_or_create(name="user")
    ct = ContentType.objects.get_for_model(User)
    perms = (
        {"name": "Can add material", "codename": "add_material", "content_type": ct},
        # {"name": "Can delete material", "codename": "delete_material", "content_type": ct},

        # 'Can change material'
        # 'Can delete material',
        # 'Can view material'
        # 'Can add category',
        # 'Can change category',
        # 'Can delete category',
        # 'Can view category'
    )

    for perm in perms:
        proj_add_perm, created = Permission.objects.get_or_create(name=perm["name"], codename=perm["codename"],
                                                                  content_type=perm["content_type"])
        user_group.permissions.add(proj_add_perm)
    return HttpResponse("you are now user.")


class Userviewset(viewsets.ModelViewSet):

    queryset = User.objects.all()
    serializer_class = serializer.UserSerializer


class Categoryviewset(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = serializer.CategorySerializer


class Materialviewset(GroupRequiredMixin, viewsets.ModelViewSet):
    group_required = [u'manager', u'user']

    queryset = Material.objects.all()
    serializer_class = serializer.MaterialSerializer


class Orderviewset(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = serializer.OrderSerializer


class UserReviewviewset(viewsets.ModelViewSet):
    queryset = UserReview.objects.all()
    serializer_class = serializer.UserReviewSerializer
