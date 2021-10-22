from core.models import Poster
from rest_framework import serializers

class PosterListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['id', 'title', 'description']


class PosterCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['title', 'description']

    def check(self, data):
        return Poster.objects.filter(**data)

    def update(self, instanse, data):
        instanse.title = data.get("title", instanse.title)
        instanse.description = data.get("description", instanse.description)
        instanse.save()
        return instanse

class PosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Poster
        fields = ['id', 'title', 'description', 'photo']
