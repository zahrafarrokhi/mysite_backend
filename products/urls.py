from django.urls import path

from . import views

urlpatterns = [
    path('', views.ProductView.as_view({'get':'list'}), name='product-list')
]
