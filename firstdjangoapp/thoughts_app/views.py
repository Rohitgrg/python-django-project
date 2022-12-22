# Import the APIView class and the Response class from Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Import the Thought model and the ThoughtSerializer
from .models import Thought
from .serializers import ThoughtSerializer

from django.shortcuts import render
from rest_framework.response import Response

# Define the ThoughtListView class


class ThoughtListView(APIView):
    serializer_class = ThoughtSerializer

    def get(self, request):
        # Get all Thoughts from the database
        thoughts = Thought.objects.all()

        # Serialize the Thoughts using the ThoughtSerializer
        serializer = self.serializer_class(thoughts, many=True)

        # Return the serialized data as a response
        return Response(serializer.data)

    def post(self, request, *args, **kwards):
        serializer = self.serializer_class(
            data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def put(self, request, pk, format=None, *args, **kwargs):
        thought_obj = Thought.objects.get(id=pk)
        serializer = self.serializer_class(
            thought_obj, data=request.data, context={'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)

    def delete(self, request, pk):
        thought_obj = Thought.objects.get(id=pk)
        thought_obj.delete()
        return Response(status=204)
