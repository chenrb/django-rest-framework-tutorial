# -*- codding: utf-8 -*-

from django.contrib.auth.models import User

from rest_framework import serializers
from snippets.models import Snippets


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippets.objects.all())
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippets-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')


class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippets-highlight', format='html')

    class Meta:
        model = Snippets
        fields = ('url', 'highlight', 'title', 'code', 'linenos', 'language', 'style', 'owner')
