from django.conf.urls import url
from django.contrib.auth import views as aviews
from . import views

urlpatterns = [
    # post views
    url(r'^login/$', views.user_login, name='login'),
    url(r'^registration/$', views.register, name='registration'),
    # url(r'^logout/$', aviews.LogoutView.as_view(), name='logout'),
    # url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    # url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    # url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    # url(r'^$', views.dashboard, name='dashboard'),
]