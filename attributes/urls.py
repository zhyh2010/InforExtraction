from django.conf.urls import url
from . import views

urlpatterns =[
	url(r'^txt/$', views.attributes_home),
	url(r'^network/$',views.attributes_network),
	url(r'^network/search/$',views.people_search),
	url(r'^txt/submit/$',views.text_upload),
]