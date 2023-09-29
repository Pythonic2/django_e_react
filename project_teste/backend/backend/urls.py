from django.urls import include, path
from rest_framework import routers
from core.views import UserViewSet, GroupViewSet, ItemViewSet, ListaViewSet

from django.contrib import admin

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)
router.register(r'items', ItemViewSet)
router.register(r'lista', ListaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),

]
