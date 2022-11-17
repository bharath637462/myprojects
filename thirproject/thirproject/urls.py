"""thirproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import to include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from dj_rest_auth.views import LoginView, LogoutView
from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenVerifyView

import thirdparty
from thirapp.urls import router
from rest_framework_simplejwt import views as jwt_views

from thirapp.views import MaterialViewset
from thirdparty import views

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('thirdparty/', include('thirdparty.urls')),
    path('thirdparty/', views.UserView.as_view()),
    path('thirdparty/<str:pk>/', views.UserDetail.as_view()),
    path('', include(router.urls)),
    path('login/', LoginView.as_view()),
    path('logout/', LogoutView.as_view()),
    path('token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
