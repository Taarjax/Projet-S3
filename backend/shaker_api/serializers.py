from rest_framework import serializers
from shaker.models import Cocktail


class CocktailSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('id', 'intitule', 'description')
        model = Cocktail