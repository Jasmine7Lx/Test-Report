from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class User(AbstractUser):
    role = models.CharField(max_length=100, blank=True)
    created_time = models.DateTimeField(auto_now_add=True)

class Demand(models.Model):
    demand_name = models.CharField(default='', max_length=100)
    DEMAND_STATUS = (
        ("no_summit", "未提测"),
        ("summit", "已提测"),
        ("completed", "已完成"),
    )
    demand_status = models.CharField(max_length=10, choices=DEMAND_STATUS)
    # 需求创建时间
    created_time = models.DateTimeField(auto_now_add=True)
    # 提测时间
    summit_test_time = models.DateTimeField(null=True, blank=True)
    # 测试完成时间
    finish_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        verbose_name = "需求"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.demand_name

class Developer(models.Model):
    DEVELOPER_TYPE = (
        ("web","前端"),
        ("background","后台"),
        ("app","移动端"),
        ("tester","测试"),
        ("product","产品")
    )
    id = models.AutoField(primary_key=True)
    demand = models.ManyToManyField(Demand)
    developer_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    password = models.CharField(max_length=40)
    role = models.CharField(max_length=20, choices=DEVELOPER_TYPE)
    created_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True, null=True, blank=True)
    class Meta:
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.developer_name

class Report(models.Model):
    REPORT_TYPE = (
        ("pc", "PC端报告"),
        ("app", "移动端报告"),
    )
    TEST_RESULT = (
        ("pass", "测试通过"),
        ("block", "测试不通过"),
        ("finish", "测试完成"),
    )
    TEST_ENV = (
        ("formal", "正式环境"),
        ("test", "测试环境"),
        ("gray", "灰度环境")
    )
    demand = models.OneToOneField(Demand)
    report_name = models.CharField(default='', max_length=100)
    report_type = models.CharField(max_length=10, choices=REPORT_TYPE, default="pc")
    test_result = models.CharField(max_length=10, choices=TEST_RESULT)
    test_env = models.CharField(max_length=10, choices=TEST_ENV)
    created_time = models.DateTimeField(auto_now_add=True)
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    class Meta:
        verbose_name = "测试报告"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.report_name

class Remain(models.Model):
    report = models.ForeignKey(Report)
    remain_content = models.TextField(null=True, blank=True)
    class Meta:
        verbose_name = "遗留问题"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.remain_content

class Config(models.Model):
    report = models.ForeignKey(Report)
    config_content = models.TextField(null=True, blank=True)
    def __str__(self):
        return self.config_content
    class Meta:
        verbose_name = "测试配置"
        verbose_name_plural = verbose_name

class Build(models.Model):
    BUILD_TYPE = (
        ("link", "网址"),
        ("version", "版本号")
    )
    report = models.ForeignKey(Report)
    build_type = models.CharField(max_length=10, choices=BUILD_TYPE, null=True, blank=True)
    build_site = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        verbose_name = "测试版本/链接"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.build_site

class Cases(models.Model):
    CASE_TYPE = (
        ("link", "链接"),
        ("file", "文件")
    )
    report = models.ForeignKey(Report)
    case_type = models.CharField(max_length=10, choices=CASE_TYPE, null=True, blank=True)
    case_content = models.CharField(max_length=200, null=True, blank=True)
    class Meta:
        verbose_name = "测试用例"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.case_content

class Bug(models.Model):
    BUG_STATUS = (
        ("no_solve","未修复"),
        ("soved","已修复"),
        ("no_need_solve","无需修复")
    )
    BUG_LEVEL = (
        ("blocker","崩溃"),
        ("critical","严重"),
        ("major","一般"),
        ("minor","次要")
    )
    demand = models.ForeignKey(Demand)
    developer = models.ForeignKey(Developer)
    bug_content = models.TextField(null=True, blank=True)
    bug_status = models.CharField(max_length=20, choices=BUG_STATUS,null=True, blank=True)
    bug_level = models.CharField(max_length=10, choices=BUG_LEVEL, null=True, blank=True)
    class Meta:
        verbose_name = "bug表"
        verbose_name_plural = verbose_name
    def __str__(self):
        return self.bug_content