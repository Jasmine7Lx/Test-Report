from rest_framework import serializers
from .models import Demand,Developer,Compat,Report
#全部需求-序列化
class DemandAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = "__all__"

#获取人员列表
class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = "__all__"

#获取兼容性列表
class CompatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compat
        fields = "__all__"

class ReportListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields ="__all__"