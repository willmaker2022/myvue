from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from storage.serializers import StorageInfoModelSerializer,InOutStorageModelSerializer
from .models import Storage,InOutStorage
from rest_framework import filters


class StorageViewSet(viewsets.ModelViewSet):
    queryset = Storage.objects.all()
    serializer_class = StorageInfoModelSerializer
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['sname']
    filter_backends = [filters.SearchFilter]
    search_fields = ['sName','sId']


#出入库记录
class InOutStorageViewSet(viewsets.ModelViewSet):
    queryset = InOutStorage.objects.all()
    serializer_class = InOutStorageModelSerializer
    filter_backends = [DjangoFilterBackend,filters.SearchFilter]
    filter_fields = ['direction']
    search_fields = ['storage__sName', 'user__username', 'product__customer']

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)