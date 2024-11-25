from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import *
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from .models import *



def members(request):
    return HttpResponse("hi")

@api_view(['GET'])
def getUsers(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getProducts(request):
    products=Product.objects.all()
    serializer=ProductSerializer(products,many=True)
    return Response(serializer.data)
@api_view(['GET'])
def getProducts_quntity(request):
    products=Product.objects.filter(quantity__gt=0).order_by("id")
    serializer=ProductSerializer(products,many=True)     
    return Response(serializer.data)
@api_view(['GET'])
def getRoles(request):
    role=Role.objects.all()
    serializer=RoleSerializer(role,many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteProduct(request,pk):
    data=request.data
    product=Product.objects.get(id=pk)
    product.delete()
    return Response("Product was deleted!")


@api_view(['GET'])
def getUser(request):
    users=User.objects.all()
    serializer=UserSerializer(users,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBill(request):
    bills=PurchaseInvoice.objects.all()
    serializer=PurchaseInvoiceSerializer(bills,many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteUser(request,pk):
    data=request.data
    user=User.objects.get(id=pk)
    user.delete()
    return Response("user was deleted!")



@api_view(['POST'])
def insertUser(request):
    data=request.data
    user=User.objects.insert(
        full_name = data['full_name'],
        date_of_birth = data['date_of_birth'],
        national_id =  data['national_id'],
        address = data['address'],
        mobile = data['mobile'],
        is_active = data['is_active'],
        role = Role.objects.get(id=data['role']),    
    )
    user.save()
    serializer=UserSerializer(user,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def insertRole(request):
    data=request.data
    role=Role.objects.insert(
      name=data['name']  
    )
    role.save()
    serializer=RoleSerializer(role,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def insertProduct(request):
    data=request.data
    product=Product.objects.insert(
        name = data['name'],
        category = data['category'],
        manufacturer =  data['manufacturer'],
        manufacture_date = data['manufacture_date'],
        expiration_date = data['expiration_date'],
        price =  data['price'],
        quantity = data['quantity']    
    )
    product.save()
    serializer=ProductSerializer(product,many=False)
    return Response(serializer.data)
@api_view(['POST'])
def insertBill(request):
    data=request.data
    purchaseInvoice=PurchaseInvoice.objects.insert(
        customer = User.objects.get(id=data['customer']),
        product =Product.objects.get(id=data['product']),
        quantity =  data['quantity'],
       
       
    )
    purchaseInvoice.save()
    serializer=PurchaseInvoiceSerializer(purchaseInvoice,many=False)
    return Response(serializer.data)
@api_view(['GET'])
def getUserByname(request,b):
    user=User.objects.filter(full_name__contains=b).order_by("id")
    serializer=UserSerializer(user,many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getBillByid(request,pk):
   bill=PurchaseInvoice.objects.filter(id=pk).order_by("id")
   serializer=PurchaseInvoiceSerializer(bill,many=True)
   return Response(serializer.data) 
@api_view(['PUT'])
def updateUser(request,pk):
    data=request.data
    user=User.objects.get(id=pk)
    serializer=UserSerializer(user,data=request.data)
    if  serializer.is_valid():
         serializer.save()
    return Response(serializer.data)
@api_view(['Get'])
def deactivate_user(request, pk):
    user = User.objects.get(id=pk)
    user.is_active = False
    user.save()
    return Response({'status': 'success'})
@api_view(['PUT'])
def updateProduct(request,pk):
    data=request.data
    product=Product.objects.get(id=pk)
    serializer=ProductSerializer(product,data=request.data)
    if  serializer.is_valid():
         serializer.save()
    return Response(serializer.data)
@api_view(['PUT'])
def updateRole(request,pk):
    data=request.data
    role=Role.objects.get(id=pk)
    serializer=RoleSerializer(role,data=request.data)
    if  serializer.is_valid():
         serializer.save()
    return Response(serializer.data)
@api_view(['GET'])
def getProductByname(request,b):
    product=Product.objects.filter(name__contains=b).order_by("id")
    serializer=ProductSerializer(product,many=True)
    return Response(serializer.data)
@api_view(['Get'])
def deleteRole(request, pk):
    role = Role.objects.get(id=pk)
    users_with_role = User.objects.filter(rolee=role)

    if users_with_role.exists():
        return Response("Role could not be deleted because it is associated with users.", status=400)

    role.delete()
    return Response("Role deleted successfully!", status=204)




@api_view(['POST'])
def purchase_product(request, pk,b):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response("Product not found.", status=404)

    if product.quantity > 0 and b<=product.quantity:
       
        product.quantity -= b
        product.save()

        

        return Response("Purchase successful.", status=200)
    else:
        return Response("Product is out of stock.", status=400)
    
    
@api_view(['DELETE'])
def delete_purchase_invoice(request, pk):
    try:
        purchase_invoice = PurchaseInvoice.objects.get(pk=pk)
    except PurchaseInvoice.DoesNotExist:
        return Response("Bill not found.", status=404)

    purchase_invoice.delete()
    return Response("Bill deleted successfully.", status=204)