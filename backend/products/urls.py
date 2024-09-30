from django.urls import path
from products import views

app_name = 'products'

urlpatterns = [
    path('', views.ProductListCreateAPIView.as_view(), name='list_create'),
    path('<int:id>/', views.ProductRetriveAPIView.as_view(), name='detail'),
    path('<int:id>/update/', views.ProductUpdateAPIView.as_view(), name='list_update'),
    path('<int:id>/delete/', views.ProductDeleteAPIView.as_view(), name='list_delete'),

]