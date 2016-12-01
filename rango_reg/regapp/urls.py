from django.conf.urls import url
from regapp import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
	url(r'^github/', views.github, name='github'),
	url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
	# url(r'^thanks/', views.thanks, name='thanks'),
]
