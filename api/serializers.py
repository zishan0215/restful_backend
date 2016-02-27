from rest_framework import serializers
from api.models import Api


class ApiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Api
        fields = ('connid', 'timeout')
