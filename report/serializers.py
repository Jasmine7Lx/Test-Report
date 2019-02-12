from rest_framework import serializers
from .models import Demand,Developer,Compat,Report,Remain,Config,Build
#全部需求-序列化
class DemandAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = "__all__"

#获取人员列表
class DeveloperListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Developer
        fields = "__all__"

#获取兼容性列表
class CompatListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compat
        fields = "__all__"

class ReportListSerializer(serializers.ModelSerializer):
    demand_name = serializers.CharField(source='demand.name')
    developer_name = serializers.CharField(source='developer.name')
    class Meta:
        model = Report
        fields = ('id','report_type','result','env','create_time','start_time','end_time','demand_name','developer_name')

# class PcReportDetailSerializer(serializers.ModelSerializer):
#     demand_name = serializers.CharField(source='demand.name')

#     class Meta:
#         model = Report
#         fields = "__all__"
    