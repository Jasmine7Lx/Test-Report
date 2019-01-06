from rest_framework import serializers
from .models import Demand,Developer
#全部需求-序列化
class DemandAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = "__all__"

class DemandListSerializer(serializers.ModelSerializer):
    class Meta:
        model =Demand
        fields = ('demand_name','created_time')

class TesterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        exclude = ('id','role','created_time','email','password','update_time','demand')

class DeveloperListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        exclude = ('id','role','created_time','email','password','update_time','demand')