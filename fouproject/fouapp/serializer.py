from .models import Category, Material, User, Order, UserReview
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
        # extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # import pdb; pdb.set_trace()
        user = super(UserSerializer, self).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()
        return user


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name")


class MaterialSerializer(serializers.ModelSerializer):
    category_details = serializers.SerializerMethodField()
    reviews_details = serializers.SerializerMethodField()

    class Meta:
        model = Material

        fields = ("id", "name", "category_details", "category", 'reviews_details',)

    def get_category_details(self, obj):
        return {'name': obj.category.name}

    def get_reviews_details(self, obj):
        return [{'review': reviews.review, 'id': reviews.user.id, 'name': reviews.user.fname} for reviews in
                obj.reviews.all()]


class OrderSerializer(serializers.ModelSerializer):
    user_details = serializers.SerializerMethodField()

    materials_details = serializers.SerializerMethodField()

    class Meta:
        model = Order
        fields = ('id', 'user', 'materials', 'user_details', 'materials_details')

    def get_user_details(self, obj):
        return {'id': obj.user.id, 'name': obj.user.fname}

    def get_materials_details(self, obj):
        return [{'id': material.id, 'name': material.name, 'category': material.category.name} for material in
                obj.materials.all()]


class UserReviewSerializer(serializers.ModelSerializer):
    materials_details = serializers.SerializerMethodField()
    user_details = serializers.SerializerMethodField()

    class Meta:
        model = UserReview
        fields = ('user', 'user_details', 'materials', 'materials_details', 'review')

    def get_user_details(self, obj):
        return {'id': obj.user.id, 'name': obj.user.fname}

    def get_materials_details(self, obj):
        return {'id': obj.materials.id, 'name': obj.materials.name}
