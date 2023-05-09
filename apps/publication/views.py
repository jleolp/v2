from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Publication, PostImage
from .serializers import PublicationSerializer, PostImageSerializer


class PublicationList(APIView):
    def get(self, request):
        publications = Publication.objects.all()
        serializer = PublicationSerializer(publications, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = PublicationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PublicationDetail(APIView):
    def get_object(self, pk):
        try:
            return Publication.objects.get(pk=pk)
        except Publication.DoesNotExist:
            return None

    def get(self, request, pk):
        publication = self.get_object(pk)
        if publication:
            serializer = PublicationSerializer(publication)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        publication = self.get_object(pk)
        if publication:
            serializer = PublicationSerializer(publication, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        publication = self.get_object(pk)
        if publication:
            publication.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)


class PostImageList(APIView):
    def post(self, request):
        serializer = PostImageSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PostImageDetail(APIView):
    def get_object(self, pk):
        try:
            return PostImage.objects.get(pk=pk)
        except PostImage.DoesNotExist:
            return None

    def get(self, request, pk):
        post_image = self.get_object(pk)
        if post_image:
            serializer = PostImageSerializer(post_image)
            return Response(serializer.data)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        post_image = self.get_object(pk)
        if post_image:
            serializer = PostImageSerializer(post_image, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        post_image = self.get_object(pk)
        if post_image:
            post_image.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)
