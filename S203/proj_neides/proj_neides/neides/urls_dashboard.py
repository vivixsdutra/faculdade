from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('client_dashboard/', views.client_dashboard, name='client_dashboard'),
    path('items/', views.items, name='items'),
    path('items/add/', views.add_item, name='add_item'),
    path('items/edit/<int:pk>/', views.edit_item, name='edit_item'),
    path('items/delete/<int:pk>/', views.delete_item, name='delete_item'),
    path('stock/', views.stock, name='stock'),
    path('reports/', views.reports, name='reports'),
    path('discounts/', views.discounts, name='discounts'),
    path('discounts/add/', views.add_discount, name='add_discount'),
    path('discounts/edit/<int:pk>/', views.edit_discount, name='edit_discount'),
    path('discounts/delete/<int:pk>/', views.delete_discount, name='delete_discount'),
]