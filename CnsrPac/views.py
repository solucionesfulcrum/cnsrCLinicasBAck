from django.shortcuts import render
from CnsrPac.models import paciente,presAnemia,admiAnemia,exclusionAnemia,movimientoAnemia
from rest_framework import viewsets, permissions, filters
from CnsrPac.serializers import pacienteSerializer,presAnemiaSerializer,admiAnemiaSerializer,exclusionAnemiaSerializer,movimientoAnemiaSerializer

# Create your views here.

class pacienteViewSet(viewsets.ModelViewSet):
    queryset = paciente.objects.all()
    serializer_class = pacienteSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=numDoc']

class presAnemiaViewSet(viewsets.ModelViewSet):
    queryset = presAnemia.objects.all().order_by('-id')
    serializer_class = presAnemiaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=paciente__id']

class admiAnemiaViewSet(viewsets.ModelViewSet):
    queryset = admiAnemia.objects.all().order_by('-id')
    serializer_class = admiAnemiaSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [filters.SearchFilter]
    search_fields = ['=presAnemia__paciente__id']

class exclusionAnemiaViewSet(viewsets.ModelViewSet):
    queryset = exclusionAnemia.objects.all().order_by('-id')
    serializer_class = exclusionAnemiaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=paciente__id']

class movimientoAnemiaViewSet(viewsets.ModelViewSet):
    queryset = movimientoAnemia.objects.all().order_by('-id')
    serializer_class = movimientoAnemiaSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['=paciente__id']
    