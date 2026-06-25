from django.shortcuts import render
from rest_framework.response import Response      # DRF Response object for API responses
from rest_framework.decorators import APIView     # Base class for class-based API views
from helloworld.serializers import PostSerializers
from rest_framework.viewsets import ModelViewSet   # Provides full CRUD operations automatically
from helloworld.models import Post
from rest_framework.permissions import IsAuthenticated
from helloworld.permissions import IsPostPossessor
# Simple API view that returns a hello world JSON response
class HelloWorldView(APIView):
    def get(self,request):
        # Handle GET requests — returns a JSON greeting 
        return Response({"message":"Hello World"})


# ModelViewSet auto-generates list, create, retrieve, update, and delete actions
class PostView(ModelViewSet):
    permission_classes=[IsAuthenticated,IsPostPossessor]
    queryset=Post.objects.all()              # Fetch all Post objects from the database
    serializer_class=PostSerializers         # Use PostSerializers to convert model ↔ JSON