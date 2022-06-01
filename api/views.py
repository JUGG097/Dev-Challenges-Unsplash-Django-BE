from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Images
from .serializers import ImageSerializer
from .renderer import ImageAPIRenderer

# Create your views here.
@api_view(["GET"])
def health_check(request):
    return Response({"success": True}, 200)


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Images.objects.all()
    serializer_class = ImageSerializer
    renderer_classes = [ImageAPIRenderer]
