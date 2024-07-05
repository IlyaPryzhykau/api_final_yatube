from rest_framework import routers

from django.urls import include, path

from .views import (GroupViewSet,
                    UserViewSet,
                    PostViewSet,
                    CommentViewSet,
                    FollowViewSet)


router = routers.DefaultRouter()
router.register('groups', GroupViewSet)
router.register('users', UserViewSet)
router.register('posts', PostViewSet)
router.register('follow', FollowViewSet, basename='follow')
router.register(r'posts/(?P<post_id>[^/.]+)/comments',
                CommentViewSet, basename='post-comments')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
