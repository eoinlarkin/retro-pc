from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('store', views.store_view, name='store'),
    path('<product_id>', views.product_detail, name='product_detail'),
]