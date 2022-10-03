from django.urls import path
from .views import BlogListView

urlpatters = [
    path("", BlogListView.as_view(), name='home')
]