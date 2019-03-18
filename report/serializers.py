from rest_framework import serializers
from .models import Demand,Developer,Compat,Report,Remain,Config,Build,Bug
#全部需求-序列化
class DisplayChoiceField(serializers.ChoiceField):
    def to_representation(self, obj):
        """返回选项的值"""
        return self._choices[obj]
class DemandAllSerializer(serializers.ModelSerializer):
    status = DisplayChoiceField(choices=(
        ("no_summit", "未提测"),
        ("summit", "已提测"),
        ("completed", "已完成")))
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
        fields = ('id','report_type','result','env','create_time','start_time','end_time','demand_name','demand_id','developer_name')
 
#获取bug所有信息（对应需求）
class BugListSerializer(serializers.ModelSerializer):
    demand_name = serializers.CharField(source='demand.name')
    status = DisplayChoiceField(choices = (
        ("no_solve","未修复"),
        ("solve","已修复"),
        ("noneed_solve","无需修复")
    ))
    class Meta:
        model = Bug
        fields = ('id', 'bug_type', 'content', 'status', 'level', 'demand_name')
