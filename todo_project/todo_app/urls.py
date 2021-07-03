from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf.urls.static import static

urlpatterns = [
    url('',views.task_view,name='task_view'),
    url('cbvtask/',views.TaskListview.as_view,name='cbvtask'),
    url('cbvdetail/<int:pk>/',views.TaskDetailview.as_view,name='cbvdetail'),
    url('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view,name='cbvupdate'),
    url('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view,name='cbvdelete'),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)