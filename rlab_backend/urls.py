from django.conf.urls import include, url
from django.contrib import admin

from . import views

urlpatterns = [
	url(r'^$', views.redirect_to_dash, name='redirect'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('fpga_dash.urls', namespace='dashboard'))
]
