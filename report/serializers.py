from rest_framework import serializers
from .models import Demand,Developer
#全部需求-序列化
class DemandAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = "__all__"
#需求列表-展示名字和创建时间
class DemandListSerializer(serializers.ModelSerializer):
    class Meta:
        model =Demand
        fields = ('name','create_time')
#获取人员列表
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        exclude = ('role','create_time','email','password','update_time','demand')
