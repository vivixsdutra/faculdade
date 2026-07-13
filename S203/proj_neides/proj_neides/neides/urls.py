from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import dashboard, admin_dashboard
from .controllers.item_controller import list_items, add_item, edit_item, delete_item, client_dashboard
from .controllers.discount_controller import list_discounts, add_discount, edit_discount, delete_discount
from .controllers.sale_controller import list_sales


urlpatterns = [
    path('', views.index, name='index'),
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
     path('', dashboard, name='dashboard'),
    path('admin_dashboard/', admin_dashboard, name='admin_dashboard'),
    path('items/', list_items, name='items'),
    path('items/add/', add_item, name='add_item'),
    path('items/edit/<int:pk>/', edit_item, name='edit_item'),
    path('items/delete/<int:pk>/', delete_item, name='delete_item'),
    path('client_dashboard/', client_dashboard, name='client_dashboard'),
    path('discounts/', list_discounts, name='discounts'),
    path('discounts/add/', add_discount, name='add_discount'),
    path('discounts/edit/<int:pk>/', edit_discount, name='edit_discount'),
    path('discounts/delete/<int:pk>/', delete_discount, name='delete_discount'),
    path('reports/', list_sales, name='reports'),
]
    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)