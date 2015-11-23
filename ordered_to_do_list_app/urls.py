from django.conf.urls import url
 
from . import views
 
urlpatterns = [

	url(r'^$', views.index, name='index'),
	url(r'^add_item/', views.add_item, name='add_item'),

]