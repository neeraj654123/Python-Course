from django.db import models


# Post model — represents a blog post stored in the database
class Post(models.Model):
    title=models.CharField(max_length=200)              # Post title, max 200 characters
    content=models.TextField()                          # Post body text, unlimited length
    created_on=models.DateTimeField(auto_now_add=True)  # Auto-set when post is first created
    updated_on=models.DateTimeField(auto_now=True)      # Auto-updated every time post is saved

    def __str__(self):
        # Display the post title in admin panel and shell
        return self.title