"""
URL configuration for blog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import Django admin module and URL routing utilities
from django.contrib import admin
from django.urls import path
# Import custom API views from the helloworld app
from helloworld.views import HelloWorldView
from rest_framework import routers
from helloworld.views import PostView

# Define URL patterns — maps URL paths to their corresponding views
urlpatterns = [
    path('admin/', admin.site.urls),         # Django admin panel
    path('hello',HelloWorldView.as_view())   # Simple hello world API endpoint
]

# Create a DRF router to auto-generate CRUD URLs for the Post model
router =routers.SimpleRouter()
router.register('posts',PostView)  # Registers /posts/ endpoint with all CRUD operations
# Append the router-generated URLs to the main urlpatterns
urlpatterns += router.urls