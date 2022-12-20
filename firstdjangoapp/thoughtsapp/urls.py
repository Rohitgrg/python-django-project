# Import the path function
from django.urls import path

# Import the ThoughtListView
from .views import ThoughtListView

# Define the URL pattern
urlpatterns = [
    path('thoughts/', ThoughtListView.as_view(), name='thought-list'),
]
