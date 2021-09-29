from CnsrPac.models import paciente,presAnemia,admiAnemia,exclusionAnemia,movimientoAnemia
from rest_framework import serializers

class pacienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = paciente
        fields = '__all__'

class presAnemiaSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = pacienteSerializer(source="paciente", read_only=True)    
    class Meta:
        model = presAnemia
        fields = '__all__'

class admiAnemiaSerializer(serializers.HyperlinkedModelSerializer):
    datosPres = presAnemiaSerializer(source="presAnemia", read_only=True)    
    class Meta:
        model = admiAnemia
        fields = '__all__'

class exclusionAnemiaSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = pacienteSerializer(source="paciente", read_only=True)   
    class Meta:
        model = exclusionAnemia
        fields = '__all__'

class movimientoAnemiaSerializer(serializers.HyperlinkedModelSerializer):
    datosPaciente = pacienteSerializer(source="paciente", read_only=True)   
    class Meta:
        model = movimientoAnemia
        fields = '__all__'