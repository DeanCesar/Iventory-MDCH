from django.urls import path
from . import views

urlpatterns=[

    path('', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff-detail'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
    path('order/', views.order, name='dashboard-order'),
    path('records/', views.records, name='dashboard-records'),
    path('order/accept/<int:order_id>/', views.accept_order, name='dashboard-accept-order'),
    path('order/deny/<int:order_id>/', views.deny_order, name='dashboard-deny-order'),
    path('order/accepted/', views.shipped_orders, name='dashboard-shipped'),
]