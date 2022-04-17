import datetime

from rest_framework import serializers
from .models import Storage,InOutStorage
from user_info.serializers import UserDescSerializer
from productplan.serializers import ProductplanSerializer

class StorageInfoModelSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='storage-detail')
    id = serializers.IntegerField(read_only=True)
    inoutstorage = serializers.SerializerMethodField()
    class Meta:
        model = Storage
        fields = "__all__"

    def get_inoutstorage(self,storage_obj):
        query_set = storage_obj.storage_inout.all()
        ret=[]
        for obj in query_set:
            if (obj.product is None) :
                    ret.append({'lcount':obj.lCount, 'user': obj.user.username, 'operateday': obj.operateday+ datetime.timedelta(hours=8), 'remark':obj.remark,
                             'customer': "", 'direction': obj.direction})
            else:
                    ret.append({'lcount': obj.lCount, 'user': obj.user.username, 'operateday': obj.operateday+ datetime.timedelta(hours=8), 'remark': obj.remark,
                         'customer': obj.product.customer,'direction': obj.direction })
        return ret


class InOutStorageModelSerializer(serializers.HyperlinkedModelSerializer):
    id = serializers.IntegerField(read_only=True)
    storage = StorageInfoModelSerializer(read_only=True)
    storage_id = serializers.IntegerField(write_only=True, allow_null=False, required=True)
    product = ProductplanSerializer(read_only=True)
    product_id = serializers.IntegerField(write_only=True, allow_null=True, required=False)
    user = UserDescSerializer(read_only=True)

    class Meta:
        model = InOutStorage
        fields = "__all__"