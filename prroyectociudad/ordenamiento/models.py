from django.db import models

# Create your models here.

class Parroquia(models.Model):
    opciones_tipo_estudiante = (
        ('urbana', 'Urbana'),
        ('rural', 'Rural'),
        )

    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=30, \
            choices=opciones_tipo_estudiante)

    def __str__(self):
        return "%s - tipo: %s" % (self.nombre,
                self.tipo)

class Barrio(models.Model):
    opciones_modulo = (
        ('1', 'Primero'),
        ('2', 'Segundo'),
        ('3', 'Tercero'),
        ('4', 'Cuarto'),
        ('5', 'Quinto'),
        )

    nombre = models.CharField(max_length=30)
    viviendas = models.IntegerField('numero de viviendas')
    num_parques = models.CharField(max_length=30, \
            choices=opciones_modulo)
    edificios = models.IntegerField('numero de edificios')
    parroquia = models.ForeignKey(Parroquia, related_name='parroquiass', on_delete=models.CASCADE)

    def __str__(self):
        return "%s | Número de Viviendas: %d | Número de Parques: %s | Número de Edificios: %d"  % (self.nombre,
                                               self.viviendas,
                                               self.num_parques,
                                               self.edificios)
