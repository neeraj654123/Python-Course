# Serializers convert model instances to JSON and validate incoming data
from rest_framework import serializers
from helloworld.models import Post


# Serializer for the Post model — handles JSON ↔ model conversion
class PostSerializers(serializers.ModelSerializer):
    class Meta():
        model =Post            # Link this serializer to the Post model
        fields='__all__'       # Include all model fields in the API response