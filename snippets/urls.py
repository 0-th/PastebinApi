from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
    prefix=r'snippets', viewset=views.SnippetViewSet, basename='snippet'
)
router.register(prefix=r'users', viewset=views.UserViewSet, basename='user')

urlpatterns = [
    path('', view=include(router.urls))
]
