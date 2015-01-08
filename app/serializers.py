__author__ = 'atomixsystem'
from django.forms import widgets
from rest_framework import serializers
from app.models import News


class NewsSerializer(serializers.Serializer):
    headline = serializers.CharField(required=False, allow_blank=True, max_length=100)
    description = serializers.CharField(style={'type': 'textarea'})

    def create(self, validated_data):

        return News.objects.create(**validated_data)