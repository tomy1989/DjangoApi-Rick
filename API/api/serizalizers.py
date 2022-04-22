#from curses import meta
#from dataclasses import field, fields
#from pyexpat import model
from rest_framework import serializers
from charachters.models import Character, Result

class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = '__all__'
        
class ResultSerializer(serializers.ModelSerializer):
    class Meta:
        model = Result
        fields = '__all__'
        
class ResponseSerializer(serializers.Serializer):
    characters = CharacterSerializer(many=True)
    result = ResultSerializer(many=False)
    