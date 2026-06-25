# Serializers convert model instances to JSON and validate incoming data
from rest_framework import serializers
from helloworld.models import Post


# Serializer for the Post model — handles JSON ↔ model conversion
class PostSerializers(serializers.ModelSerializer):
    created_by=serializers.CharField(source='created_by.username',read_only=True)
    class Meta():
        model =Post            # Link this serializer to the Post model
        fields='__all__'       # Include all model fields in the API response
        #read_only_fields=('created_by',)
    
    def create(self, validated_data):
        validated_data['created_by']=self.context['request'].user
        return Post.objects.create(**validated_data)