from django.db import models

class Tipo_Documento(models.Model):
    tipo_documento = models.CharField(max_length = 2)   

class Persona(models.Model):
    documento = models.CharField(max_length = 12)
    idtipo_documento = models.ForeignKey(Tipo_Documento,on_delete=models.CASCADE)
    nombre = models.CharField(max_length = 45)
    apellido = models.CharField(max_length = 45)
    email = models.EmailField(max_length = 100)
    telefono = models.CharField(max_length = 10)

class Proyecto(models.Model):
    proyecto = models.CharField(max_length = 100)
    descripcion = models.TextField()
    idpersona = models.ForeignKey(Persona, on_delete = models.CASCADE)

class Estado_Tarea(models.Model):
    estado = models.CharField(max_length = 10)

class Tarea(models.Model):
    tarea = models.CharField(max_length = 25)
    descripcion = models.TextField()
    idestado = models.ForeignKey(Estado_Tarea,on_delete = models.CASCADE)
    idproyecto = models.ForeignKey(Proyecto, on_delete = models.CASCADE)
    idpersona = models.ForeignKey(Persona, on_delete=models.CASCADE)