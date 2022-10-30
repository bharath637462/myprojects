from django.urls import path

from . import views

app_name = "firstapp"

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('firstapp/<pk>/', views.DetailView.as_view(), name='detail'),
    path('add/', views.Createview.as_view(), name='add'),
    path('choice/', views.Choiceview.as_view(), name='choice'),
    path('delete/<pk>/', views.DeleteView.as_view(), name='delete'),
    path('update/<pk>/', views.UpdateView.as_view(), name='update'),

    path('<pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<pk>/vote/', views.vote, name='vote'),

]
