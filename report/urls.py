from django.conf.urls import url
from . import views
from django.views.generic import TemplateView

app_name = 'report'
urlpatterns = [
    url(r'^$',TemplateView.as_view(template_name="index.html")),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
]
