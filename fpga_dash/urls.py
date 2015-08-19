from django.conf.urls import include, url
from django.contrib import admin

from dajaxice.core import dajaxice_autodiscover, dajaxice_config
dajaxice_autodiscover()

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^linkage$', views.linkage, name='linkage'),
    url(r'^bitstream$', views.ul_bitstream, name="ul_bitstream"),
    url(r'^audio$', views.ul_audio, name="ul_audio"),
    url(dajaxice_config.dajaxice_url, include('dajaxice.urls')),
]
