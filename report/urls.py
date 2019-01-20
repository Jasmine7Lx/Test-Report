from django.conf.urls import url
from . import views
# from django.views.generic import TemplateView

app_name = 'report'
urlpatterns = [
    # url(r'^',TemplateView.as_view(template_name="index.html")),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    # url(r'^demo/$', views.demo, name='demo'),
    url(r'^demand$', views.getDemandAll, name='demand'),
    url(r'^tester', views.getTesterList, name='tester'),
    url(r'^developer$', views.getDeveloperList, name='developer'),
    url(r'^product$', views.getProductList, name='product'),
    url(r'^report$', views.Report, name='report')
]
