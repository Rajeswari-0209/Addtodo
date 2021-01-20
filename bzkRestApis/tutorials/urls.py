from django.conf.urls import url 
from tutorials import views 
 
urlpatterns = [ 
    url(r'^tutorials$', views.tutorial_list),
    url(r'^tutorials/(?P<pk>[0-9]+)$', views.tutorial_detail),
    url(r'^tutorials/published$', views.tutorial_list_published)
   
   
   
   
]
 
 
 
 