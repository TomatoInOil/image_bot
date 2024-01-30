from rest_framework import status
from rest_framework.generics import ListCreateAPIView
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer

from images.models import Image


class ImageSerializer(ModelSerializer):
    class Meta:
        model = Image
        fields = ("photo", "file_id")


class ImageView(ListCreateAPIView):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
