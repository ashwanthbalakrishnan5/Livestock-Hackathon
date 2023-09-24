from django.urls import path, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()

router.register("animals", AnimalViewSet)
router.register("breeds", BreedViewSet)
router.register("info", InfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
