from django.urls import path # type: ignore
from .views import MenuList, MenuItemDetail

urlpatterns = [
    path('', MenuList.as_view(), name='home'),
    path('menu/<int:pk>/', MenuItemDetail.as_view(), name='menu_item'),
]
