from rest_framework import serializers
from .models import Demande
from accounts.serializers import UserMeSerializer
from rest_framework.reverse import reverse
from django.utils.text import slugify


class DemandeSerailizers(serializers.ModelSerializer):
    owner_info = UserMeSerializer(source='owner', read_only=True, many=False)
    owner = serializers.HiddenField(default=serializers.CurrentUserDefault())
    links = serializers.SerializerMethodField('_links')
    slug = serializers.SerializerMethodField('_slug')

    class Meta:
        model = Demande
        exclude = ['terminee']

    @staticmethod
    def _slug(obj):
        return slugify(obj.title)

    @staticmethod
    def _links(obj):
        return {
            'self': reverse('demande-details', args=[obj.pk]),
            'update': reverse('demande-update', args=[obj.pk]),
            'patch': reverse('demande-patch', args=[obj.pk]),
            'delete': reverse('demande-delete', args=[obj.pk]),
        }
