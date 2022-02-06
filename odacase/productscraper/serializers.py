from rest_framework import serializers
from .models import PSConfig, PSAttribute

class PSConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSConfig
        fields = ('id', 'base_url', 'whitelist', 'product_xpath')

class PSAttributeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSAttribute
        fields = ('id', 'ps_config', 'attribute_name', 'attribute_xpath')
