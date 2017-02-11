
from django.conf.urls import url
from django.contrib import admin
from blog import views 
#from django.contrib.staticfiles.urls import staticfiles_urlpatterns
 
urlpatterns = [
  
     url(r'^$', views.base, name='base'),
     url(r'^$', views.post_list, name='post_list'),
    url(r'^post/new/$', views.post_new, name='post_new'),
    
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
      url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),
     url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'),
     url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
     url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'),
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),
     url(r'^books/$', views.books, name='books'),
     url(r'^journals/$', views.journals, name='journals'),
     url(r'^Magazine/$', views.Magazine, name='Magazine'),
     url(r'^contact/$', views.contact, name='contact'),
     url(r'^blog1/$', views.blog1, name='blog1'),
 


]


