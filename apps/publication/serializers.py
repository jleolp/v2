from rest_framework import serializers
from .models import Publication, PostImage


class PostImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostImage
        fields = ('image',)


class PublicationSerializer(serializers.ModelSerializer):
    postImages = PostImageSerializer(many=True, read_only=True)

    class Meta:
        model = Publication
        fields = '__all__'

    def create(self, validated_data):
        images = validated_data.pop('postImages', [])
        publication = Publication.objects.create(**validated_data)
        for image in images:
            PostImage.objects.create(publication=publication, **image)
        return publication

    def update(self, instance, validated_data):
        images = validated_data.pop('postImages', [])
        for image in images:
            PostImage.objects.create(publication=instance, **image)
        return super().update(instance, validated_data)

