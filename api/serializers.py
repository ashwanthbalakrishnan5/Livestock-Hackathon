from rest_framework import serializers
from .models import *


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animals
        fields = "__all__"


class BreedSerializer(serializers.ModelSerializer):
    # animal = AnimalSerializer()

    class Meta:
        model = Breeds
        fields = "__all__"


class InfoSerializer(serializers.ModelSerializer):
    # breed = BreedSerializer()

    class Meta:
        model = Info
        fields = "__all__"
