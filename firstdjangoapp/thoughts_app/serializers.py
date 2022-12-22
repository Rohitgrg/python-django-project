# Import the serializers module from Django Rest Framework
from rest_framework import serializers

# Import the Thought model
from .models import Thought

# Define the ThoughtSerializer class


class ThoughtSerializer(serializers.ModelSerializer):
    # Specify the fields that should be serialized
    class Meta:
        model = Thought
        fields = ['id', 'main_text']
