from django.conf.urls import url
from api import views

urlpatterns = [
    url(r'^serverStatus$', views.server_status),
    url(r'^request', views.process_request),
    url(r'^kill', views.kill),
]
