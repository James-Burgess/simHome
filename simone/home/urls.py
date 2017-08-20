from django.conf.urls import url, include
from . import views
from models import state

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^submit/1$', views.submit1 ),





	url(r'^submit/2', views.submit2),
	url(r'^submit/3', views.submit3),
	url(r'^submit/4', views.submit4),
	url(r'^submit/5', views.submit5),
	url(r'^submit/6', views.submit6),
	url(r'^submit/7', views.submit7),
	url(r'^submit/8', views.submit8),

	]