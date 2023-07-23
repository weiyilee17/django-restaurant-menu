from django.urls import path
from . import views

urlpatterns = [
    path('', views.DishList.as_view(), name='home'),
    path('dish_detail/<int:pk>/', views.DishDetail.as_view(), name='dish_detail_page'),
]
