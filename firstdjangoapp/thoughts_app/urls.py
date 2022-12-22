# Import the path function
from django.urls import path

# Import the ThoughtListView
from .views import ThoughtListView

app_name = "thoughts_app"

# Define the URL pattern
urlpatterns = [
    path('thought/', ThoughtListView.as_view(), name='thought'),
    path('thought/<int:pk>/', ThoughtListView.as_view(), name='thought'),

]
