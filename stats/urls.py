from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^user_stats$', views.user_stats, name='user_stats')
]
