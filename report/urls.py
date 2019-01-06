from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'report'
urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name="index.html")),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^demo/$', views.demo, name='demo'),
    url(r'^get_demand_all/$', views.getDemandAll, name='get_demand_all'),
    url(r'^get_tester_all/$', views.getTesterList, name='get_tester_all'),
    url(r'^get_developer_all/$', views.getDeveloperList, name='get_developer_all'),
]
