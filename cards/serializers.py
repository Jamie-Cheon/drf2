from django.contrib.auth.models import User
from cards.models import Card
from rest_framework import serializers


class CardSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Card
        fields = ['id', 'owner', 'name']


class UserSerializer(serializers.ModelSerializer):
    cards = CardSerializer(many=True, source='card_set')

    class Meta:
        model = User
        fields = ['id', 'username', 'cards']





