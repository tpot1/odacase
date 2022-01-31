from rest_framework import serializers
from .models import PSConfig

class PSConfigSerializer(serializers.ModelSerializer):
    class Meta:
        model = PSConfig
        fields = ('id', 'base_url', 'whitelist', 'product_xpath')
