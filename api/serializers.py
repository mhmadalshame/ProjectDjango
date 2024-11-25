from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
        depth  = 1      
class RoleSerializer(ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'                                

class PurchaseInvoiceSerializer(ModelSerializer):
    class Meta:
        model = PurchaseInvoice
        fields = '__all__'
        depth =1
        
