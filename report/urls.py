from django.conf.urls import url
from . import views
# from django.views.generic import TemplateView

app_name = 'report'
urlpatterns = [
    # url(r'^',TemplateView.as_view(template_name="index.html")),
    url(r'^login$', views.Login, name='login'),
    # url(r'^logout/$', views.logout, name='logout'),
    url(r'^demand$', views.getDemandAll, name='demand'),     #获取所有需求
    url(r'^getdemand',views.getDemandReport, name='getdemand'),   #获取已提测的需求
    url(r'^developerall', views.getDeveloperAll, name='developerall'),    #获取需求对应的产研测人员
    url(r'^tester', views.getTesterList, name='tester'),        #获取所有测试人员信息
    url(r'^developer$', views.getDeveloperList, name='developer'),      #获取所有开发人员信息
    url(r'^product$', views.getProductList, name='product'),        #获取所有产品人员信息
    url(r'^pcreport$', views.PcReport, name='pcreport'),            #新增PC端报告&获取对应报告的详情页信息
    url(r'^appreport$', views.AppReport, name='appreport'),       #新增移动端报告&获取对应报告的详情页信息
    url(r'^computer$', views.getComputerList, name='computer'),     #获取电脑兼容性列表
    url(r'^browser$', views.getBrowserList, name='browser'),        #获取浏览器兼容性列表
    url(r'^phone$', views.getPhoneList, name='phone'),              #暂时未做，同pcreport
    url(r'^reportlistall$', views.getReportListAll, name="reportlistall"),          #获取全部报告列表需要展示的对应信息
    url(r'^reportlistpc$', views.getReportListPc, name="reportlistpc"),          #获得PC端报告列表需要展示的对应信息
    url(r'^reportlistapp$', views.getReportListApp, name="reportlistapp"),          #获得移动端报告列表需要展示的对应信息
    url(r'^demandlist$', views.getDemandList, name='demandlist'),        #新增需求&获取对应需求的详细信息
    url(r'^editdemand$',views.editDemand, name="editdemand"),           #编辑需求
    url(r'^deletedemand$',views.deleteDemand, name="deletedemand"),
    url(r'^buglist$', views.getBugList, name='buglist')        #获取所有bug信息
]
