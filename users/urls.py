from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    # url(r'^signup/$', views.signup, name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate, name='activate'),
    url(r'^(?P<username>[a-zA-Z0-9]+)$', views.get_user_profile, name='profile'),
    url(r'^(?P<username>[a-zA-Z0-9]+)/edit$', views.edit_user_profile, name='edit_profile'),
    url(r'^(?P<pk>[0-9]+)/edit2$', views.AuthorUpdate.as_view(), name='edit_profile2'),
]
