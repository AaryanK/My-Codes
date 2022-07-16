from rest_framework import serializers
from .models import *

class CustomerSerializer(serializers.ModelSerializer):
	class Meta:
		model = Customer
		fields = ('id','user','first_name','last_name','email','created_on','customer_token')
		