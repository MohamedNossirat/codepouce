from abc import ABC

from rest_framework import serializers
from .models import CodePouceUser
import base64
from django.core.files.uploadedfile import InMemoryUploadedFile
from rest_framework.reverse import reverse


def _convert_to_string(f_object: InMemoryUploadedFile):
    _imagestr = str(base64.b64encode(f_object.read()).decode())
    _content = f_object.content_type
    return "data:" + _content + ";base64," + _imagestr


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    pic = serializers.FileField(write_only=True)

    class Meta:
        model = CodePouceUser
        fields = ['id', 'email', 'photo', 'first_name', 'last_name', 'password', 'pic', 'date_naissance', 'langues',
                  'ville', 'telephone']
        extra_kwargs = {
            'photo': {'read_only': True}
        }

    def get_update_url(self, obj):
        return reverse('update_user', args=[obj.pk])

    def create(self, validated_data):
        print(self.context['request'].data)
        password = validated_data.pop('password')
        photo = validated_data.pop('pic')
        user = CodePouceUser.objects.create(**validated_data)
        user.set_password(password)
        user.photo = _convert_to_string(photo)
        user.save()
        return user


class UserUpdateSerializer(serializers.ModelSerializer):
    pic = serializers.FileField(write_only=True, required=False)
    update_url = serializers.SerializerMethodField()

    class Meta:
        model = CodePouceUser
        fields = ['id', 'email', 'photo', 'first_name', 'last_name', 'pic', 'date_naissance', 'langues',
                  'ville', 'telephone', 'update_url']
        extra_kwargs = {
            'photo': {'read_only': True}
        }

    def get_update_url(self, obj):
        return reverse('update_user', args=[obj.pk])

    def update(self, instance, validated_data):
        photo = validated_data.get('pic')
        instance.email = validated_data.get('email', instance.email)
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.date_naissance = validated_data.get('date_naissance', instance.date_naissance)
        instance.langues = validated_data.get('langues', instance.langues)
        instance.ville = validated_data.get('ville', instance.ville)
        instance.telephone = validated_data.get('telephone', instance.telephone)
        if photo is not None:
            instance.photo = _convert_to_string(photo)
        instance.save()
        return instance


class UserMeSerializer(serializers.ModelSerializer):
    links = serializers.SerializerMethodField('_links')

    class Meta:
        model = CodePouceUser
        fields = ['links', 'email', 'first_name', 'last_name', 'photo', 'ville', 'langues', 'telephone']

    @staticmethod
    def _links(obj):
        return {
            'update': reverse('update-user', args=[obj.pk]),
            'delete': reverse('delete-user', args=[obj.pk]),
        }
