from rest_framework import serializers
from .models import Organizations, Systems

class OrganizationsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Organizations
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
        }


class SystemsSerializers(serializers.ModelSerializer):
    organization = OrganizationsSerializers(read_only=True, source='org_id')
    class Meta:
        model = Systems
        fields = '__all__'

        extra_kwargs = {
            'id': {'read_only': True},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'org_id': {'write_only': True}
        }