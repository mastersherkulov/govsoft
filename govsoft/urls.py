from rest_framework import routers
from django.urls import path, include
from govsoft.views import *

router = routers.SimpleRouter()
router.register(r'tashkilotlar', OrganizationsViewSet)
router.register(r'tizimlar', SystemsViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("export/tashkilotlar.csv", export_organizations_csv),
    path("export/tizimlar.csv", export_systems_csv),
]