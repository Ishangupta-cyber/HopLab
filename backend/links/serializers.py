from rest_framework import serializers
from .models import Link

class ShortenSerializer(serializers.Serializer):
    url = serializers.URLField(max_length=2048)

class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = ['original_url', 'short_code', 'click_count', 'created_at']