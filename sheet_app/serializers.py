from rest_framework import serializers 
from .models import Random_

class Random_Serializer(serializers.ModelSerializer): 
    class Meta: 
        model = Random_ 
        fields = '__all__' 
