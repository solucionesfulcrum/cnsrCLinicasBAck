from django.shortcuts import render
from ServLisLab.models import Solexalab,Solexalabcps
from rest_framework import viewsets, permissions, filters
from ServLisLab.serializers import SolexalabSerializer,SolexalabcpsSerializer
# Create your views here.

class SolexalabViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Solexalab.objects.all()
    serializer_class = SolexalabSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['soleqppacdocidennum']

class SolexalabcpsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Solexalabcps.objects.all()
    serializer_class = SolexalabcpsSerializer
    permission_classes = [permissions.IsAuthenticated]    
    filter_backends = [filters.SearchFilter]
    search_fields = ['soleqpexanum__soleqppacdocidennum']