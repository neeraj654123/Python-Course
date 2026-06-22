from django.contrib import admin
from helloworld.models import Post

# Register the Post model so it appears in the Django admin panel
admin.site.register(Post)