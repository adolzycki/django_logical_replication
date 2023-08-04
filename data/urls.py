from django.conf.urls import url, include
from rest_framework import routers

from .views import DataViewSet, AnnotationViewSet


router = routers.DefaultRouter()
router.register(r'data', DataViewSet)
router.register(r'annotation', AnnotationViewSet)

urlpatterns = [
    url(r'^', include(router.urls))
]
