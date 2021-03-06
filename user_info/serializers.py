from rest_framework import serializers
from django.contrib.auth.models import User


class UserDescSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'last_login',
            'date_joined',
        ]

class UserRegisterSerializer(serializers.ModelSerializer):
    url = serializers.HyperlinkedIdentityField(view_name='user-detail',lookup_field='username')

    class Meta:
        model = User
        fields = [
            'url',
            'id',
            'username',
            'password',
        ]
        extra_kwargs = {
            'password':{'write_only':True}
        }

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

    def update(self, instance, validated_data):
        if 'password' in validated_data:
            password = validated_data.pop('password')
            instance.set_password(password)
        return super().update(instance,validated_data)