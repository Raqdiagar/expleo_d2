from dataclasses import dataclass
from rest_framework import serializers
from entries.models import EntryModel

class EntrySerializer(serializers.Serializer):
    id = serializers.ReadOnlyField()
    concept = serializers.CharField()
    amount = serializers.FloatField()
    datetime = serializers.DateTimeField()
    
    def create(self, validated_data):
        # Voy a salvar a validated datacass
        instance = EntryModel(
            datetime=validated_data.get("datetime"),
            concept = validated_data.get("concept"),
            amount = validated_data.get("amount")
        )
        
        instance.save()
        return instance
        
    def update(self, instance, validate_data):
        # Voy a modificar mi instancia con validated data
        pass