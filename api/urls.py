from django.urls import path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
    path('getusers/',views.getUsers),
    path('getproducts/',views.getProducts),
    path('productsquntityabovezero/',views.getProducts_quntity),
    path('getbills/',views.getBill),
    path('roles/',views.getRoles),
    path('insertUser/',views.insertUser),
    path('insertProducr/',views.insertProduct),
    path('insertRole/',views.insertRole),
    path('insertBill/',views.insertBill),
    path('updateUser/<str:pk>/',views.updateUser),
    path('updateProduct/<str:pk>/',views.updateProduct),
    path('updateRole/<str:pk>/',views.updateRole),
    path('deactivateUser/<str:pk>/',views.deactivate_user),
    path('deletePrduct/<str:pk>/',views.deleteProduct),
    path('deleteRole/<str:pk>/',views.deleteRole),  
    path('getbillbyid/<str:pk>/',views.getBillByid),
    path('getproductbyname/<str:b>/',views.getProductByname),
    
    path('purchase_product/<str:pk>/<int:b>/',views.purchase_product),
    path('delete_purchase_invoice/<str:pk>/',views.delete_purchase_invoice),   
]