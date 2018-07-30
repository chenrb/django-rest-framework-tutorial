# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from snippets import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
# urlpatterns = format_suffix_patterns(urlpatterns)
# urlpatterns = [
#     url(r'^snippets/$', views.SnippetList.as_view(), name='snippet-list'),
#     url(r'^snippets/(?P<pk>\d+)/$', views.SnippetDetail.as_view(), name='snippets-detail'),
#     url(r'^users/$', views.UserList.as_view(), name='user-list'),
#     url(r'^users/(?P<pk>\d+)/$', views.UserDetail.as_view(), name='user-detail'),
#     url(r'^$', views.api_root),
#     url(r'^snippets/(?P<pk>\d+)/highlight/$', views.SnippetHighlight.as_view(), name='snippet-highlight'),
# ]
#
# urlpatterns = format_suffix_patterns(urlpatterns)
#
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# ]
