from django.views.decorators.csrf import csrf_exempt

# Import the APIView class and the Response class from Django Rest Framework
from rest_framework.views import APIView
from rest_framework.response import Response

# Import the Thought model and the ThoughtSerializer
from .models import Thought
from .serializers import ThoughtSerializer

from django.shortcuts import render
from django.http import HttpResponse

# Define the ThoughtListView class


class ThoughtListView(APIView):
    def get(self, request):
        # Get all Thoughts from the database
        thoughts = Thought.objects.all()

        # Serialize the Thoughts using the ThoughtSerializer
        serializer = ThoughtSerializer(thoughts, many=True)

        # Return the serialized data as a response
        return Response(serializer.data)

    @csrf_exempt
    def create_thought(request):
        if request.method == 'POST':
            serializer = ThoughtSerializer(data=request.POST)
            if serializer.is_valid():
                serializer.save()
                return HttpResponse(serializer.data, status=201)
            return HttpResponse(serializer.errors, status=400)
