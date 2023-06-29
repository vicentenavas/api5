from django.urls import re_path
from info import views


urlpatterns=[
    re_path(r'^servizio$', views.servizioApi),
    re_path(r'^servizio/([0-9]+)$', views.servizioApi),
    re_path(r'^socio$', views.socioApi),
    re_path(r'^socio/([0-9]+)$', views.socioApi),
]
