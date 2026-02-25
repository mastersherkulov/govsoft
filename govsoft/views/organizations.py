from rest_framework import viewsets
from govsoft.serializers import OrganizationsSerializers
from govsoft.models import Organizations

class OrganizationsViewSet(viewsets.ModelViewSet):
    queryset = Organizations.objects.all()
    serializer_class = OrganizationsSerializers
    allowed_methods = ['GET', 'PUT', 'POST', 'DELETE']
    http_method_names = ['get', 'put', 'post', 'delete']
    filterset_fields = ['org_code', 'org_name', 'is_active']
    