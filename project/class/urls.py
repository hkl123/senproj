from django.conf.urls import url
from . import views


urlpatterns = [

    # index is like home ~ /class/
    url(r'^$', views.Index.as_view(), name='index'),


    url(r'class/home/add/$', views.MakeClass.as_view(), name='makeclass'),

 #   url(r'class/login/$', views.login.as_view(), name='login'),

    url(r'class/(?P<pk>[0-9]+)/updateclass/$', views.UpdateClass.as_view(), name='updateclass'),

    url(r'class/(?P<pk>[0-9]+)/Assignments/makeassignment', views.MakeAssignment.as_view(), name='makeassignment'),

    url(r'class/(?P<pk>[0-9]+)/Assignment/updateassignment/$', views.UpdateAssignment.as_view(), name='updateassignment'),

    url(r'class/(?P<pk>[0-9]+)/Calendar/makecalentry', views.MakeCalEntry.as_view(), name='makecalentry'),

    url(r'class/(?P<pk>[0-9]+)/Calendar/updatecalentry/$', views.UpdateCalEntry.as_view(),
        name='updatecalentry'),

    url(r'class/(?P<pk>[0-9]+)/deleteclass/$', views.DeleteClass.as_view(), name='deleteclass'),

    url(r'^signup/$', views.SignUpPage.as_view(), name='signup'),

    # /class/{classID}
    url(r'^(?P<pk>[0-9]+)/$', views.ClassInfo.as_view(), name='class_info'),


    url(r'^(home)/$', views.Home.as_view(), name='home'),


    url(r'^(?P<pk>[0-9]+)/Assignments/$', views.Assignments.as_view(), name='assignments'),


    url(r'^(?P<pk>[0-9]+)/studentlist/$', views.StudentList.as_view(), name='studentlist'),


    url(r'^(?P<pk>[0-9]+)/Points/$', views.Points.as_view(), name='points'),


    url(r'^(?P<pk>[0-9]+)/Store/$', views.Store.as_view(), name='store'),


    url(r'class/(?P<pk>[0-9]+)/Store/makeitem', views.MakeItem.as_view(), name='makeitem'),


    url(r'class/(?P<pk>[0-9]+)/Store/updateitem/$', views.UpdateItem.as_view(), name='updateitem'),


    url(r'^(?P<pk>[0-9]+)/Calendar/$', views.Calendar.as_view(), name='calendar'),

]