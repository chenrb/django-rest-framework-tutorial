# -*- codding: utf-8 -*-

from django.contrib.auth.models import User

from rest_framework import serializers
from snippets.models import Snippets


class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippets.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')


# ModelSerializers
class SnippetSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Snippets
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')
