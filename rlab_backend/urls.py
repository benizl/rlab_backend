from django.conf.urls import include, url
from django.contrib import admin

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from . import views

urlpatterns = [
    url(r'^$', views.redirect_to_dash, name='redirect'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^dashboard/', include('fpga_dash.urls', namespace='dashboard')),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
]
