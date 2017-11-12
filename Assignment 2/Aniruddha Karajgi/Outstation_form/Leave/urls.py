from django.conf.urls import url
from . import views

app_name = 'Leave'

urlpatterns = [
    url(r'^$', views.LeaveListView.as_view(), name="leave_list_view"),

    url(r'^register/$', views.Register.as_view(), name="register"),

    url(r'^login/$', views.login_view, name="login_view"),

    url(r'^logout/$', views.logout_view, name="logout_view"),

    url(r'^leave/add/$', views.LeaveAddView.as_view(), name="leave_add_view"),

    url(r'^leave/approve/chief_view/$', views.chief_view, name="chief_view"),

    url(r'^leave/approve/$', views.leave_approve_view, name="leave_approve_view"),
]
