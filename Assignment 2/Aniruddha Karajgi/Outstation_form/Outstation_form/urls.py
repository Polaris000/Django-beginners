from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^', include('Leave.urls')),

    

    url(r'^accounts/', include('allauth.urls')),
    
]

 # allauth urls

"""
url(r"^signup/$", allauth_views.signup, name="account_signup"),

url(r"^accounts/login/$", allauth_views.login, name="account_login"),

url(r"^accounts/logout/$", allauth_views.logout, name="account_logout"),

url(r"^accounts/password/change/$", allauth_views.password_change, name="account_change_password"),

url(r"^accounts/password/set/$", allauth_views.password_set, name="account_set_password"),

url(r"^accounts/inactive/$", allauth_views.account_inactive, name="account_inactive"),"""
