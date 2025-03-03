from django.urls import path # type: ignore

from . import views

urlpatterns = [
    path('', views.MenuList.as_view(), name='home'),
    path('<int:pk>/', views.MenuItemDetail.as_view(), name='detail'),
]