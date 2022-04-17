import datetime
from rest_framework import serializers
from .models import Service
from user_info.serializers import UserDescSerializer
from productplan.serializers import ProductplanSerializer

#订单计划
class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    orderid = ProductplanSerializer(read_only=True)
    orderid_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    user = UserDescSerializer(read_only=True)
    class Meta:
        model = Service
        fields = '__all__'
