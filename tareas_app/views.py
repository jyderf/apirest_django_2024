from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Persona, Proyecto, Tarea, Tipo_Documento, Estado_Tarea
from .serializers import PersonaSerializer, ProyectoSerializer, TareaSerializer, Tipo_DocumentoSerializer, Estado_TareaSerializer

class PersonaViewSet(viewsets.ModelViewSet):
    queryset = Persona.objects.all()
    serializer_class = PersonaSerializer

class ProyectoViewSet(viewsets.ModelViewSet):
    queryset = Proyecto.objects.all()
    serializer_class = ProyectoSerializer

class TareaViewSet(viewsets.ModelViewSet):
    queryset = Tarea.objects.all()
    serializer_class = TareaSerializer

class Tipo_DocumentoViewSet(viewsets.ModelViewSet):
    queryset = Tipo_Documento.objects.all()
    serializer_class = Tipo_DocumentoSerializer

class Estado_TareaViewSet(viewsets.ModelViewSet):
    queryset = Estado_Tarea.objects.all()
    serializer_class = Estado_TareaSerializer

 