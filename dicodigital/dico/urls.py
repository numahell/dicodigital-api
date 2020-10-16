from django.urls import include, path

from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'word', views.Word)
router.register(r'definition', views.Definition)
router.register(r'vote', views.Vote)

urlpatterns = [
    path('', include(router.urls)),
    path(
        'api-auth/',
        include('rest_framework.urls', namespace='rest_framework')
    )
]
