from rest_framework import serializers
from .models import Actor, Movie


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = '__all__'




class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True)
    class Meta:
        model = Movie
        fields = '__all__'
        


class MovieCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie


class ActorCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Actor
        exclude = ['id']