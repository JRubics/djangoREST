from rest_framework import serializers
from restapp.models import Hotel

class HotelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hotel
        fields = ('id', 'title', 'star_num')

    # def create(self, validated_data):
    #     """
    #     Create and return a new `Snippet` instance, given the validated data.
    #     """
    #     return Hotel.objects.create(**validated_data)

    # def update(self, instance, validated_data):
    #     """
    #     Update and return an existing `Snippet` instance, given the validated data.
    #     """
    #     instance.title = validated_data.get('title', instance.title)
    #     instance.star_num = validated_data.get('star_num', instance.star_num)
    #     instance.save()
    #     return instance