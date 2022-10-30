from django.contrib import admin

from .models import Material, Category, Order, User, UserReview

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Material)
admin.site.register(Order)
admin.site.register(UserReview)
