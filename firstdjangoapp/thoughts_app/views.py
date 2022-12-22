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
        serializer = self.serializer_class(data=request.POST)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(self.serializer_class(serializer.data), status=201)
        return Response({
            'error': {
                'email': "This field is required."
            }
        }, status=400)
