from rest_framework import viewsets
from govsoft.serializers import SystemsSerializers
from govsoft.models import Systems

class SystemsViewSet(viewsets.ModelViewSet):
    queryset = Systems.objects.all()
    serializer_class = SystemsSerializers
    allowed_methods = ['GET', 'PUT', 'POST', 'DELETE']
    http_method_names = ['get', 'put', 'post', 'delete']
    filterset_fields = ['system_type', 'system_name', 'status', 'org_id', 'org_id__org_name', 'org_id__org_code']