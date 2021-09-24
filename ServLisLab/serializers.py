from ServLisLab.models import Solexalab,Solexalabcps
from rest_framework import serializers

class SolexalabSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Solexalab
        fields = '__all__'

class SolexalabcpsSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = SolexalabSerializer(source="soleqpexanum", read_only=True)    
    class Meta:
        model = Solexalabcps
        fields = '__all__'