from django.db import models
from django.contrib.auth.models import User 
# Create your models here.


class Estudiante(models.Model):
    idEstudiante = models.CharField(primary_key=True,max_length=15)
    nombre = models.CharField(max_length=50)

    
class Materia(models.Model):
    nombreMateria = models.CharField(max_length=50)
    semestre=models.IntegerField()
    nombreProfesor=models.CharField(max_length=50)
    cantCreditos=models.IntegerField()
    user =models.ForeignKey(User,on_delete=models.CASCADE)
    
class Semestre(models.Model):
    numerosemestre = models.IntegerField()
    creditos=models.IntegerField()
    promedio=models.IntegerField()
    cantMaterias=models.IntegerField()
    

