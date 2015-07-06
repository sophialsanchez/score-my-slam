from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^round/', views.round, name='round'),
	url(r'^final/', views.final, name='final'),

]