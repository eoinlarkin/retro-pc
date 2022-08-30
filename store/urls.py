from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('store', views.store_view, name='store'),
    path('<int:product_id>/', views.product_detail, name='product_detail'),
    path('add/', views.add_new_product, name='add_new_product'),
    path('edit/<int:product_id>/', views.edit_product, name='edit_product'),
    path('delete/<int:product_id>/', views.delete_product, name='delete_product'),

]