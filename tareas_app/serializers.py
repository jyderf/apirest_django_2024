from rest_framework import serializers
from .models import Persona, Proyecto, Tarea, Tipo_Documento, Estado_Tarea

class PersonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = '__all__'

class ProyectoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Proyecto
        fields = '__all__'

class TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tarea
        fields = '__all__'

class Tipo_DocumentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Documento
        fields = '__all__'

class Estado_TareaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_Tarea
        fields = '__all__'