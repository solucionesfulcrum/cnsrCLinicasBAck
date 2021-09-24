from django.db import models

# Create your models here.


class paciente(models.Model):
    tipoDoc = models.CharField(max_length=30)
    numDoc = models.CharField(max_length=10)
    apePat = models.CharField(max_length=30)
    apeMat = models.CharField(max_length=30)    
    nombres = models.CharField(max_length=50)
    fechaNac = models.DateField()
    sexo = models.CharField(max_length=15)
    estado = models.CharField(max_length=5, default=1)

    def __str__(self):
        return self.numDoc

class presAnemia(models.Model):
    paciente = models.ForeignKey(paciente, on_delete=models.CASCADE)
    fechaPres = models.DateField()
    nomNefro = models.CharField(max_length=30)
    medPres = models.CharField(max_length=30)
    dosisPres = models.IntegerField()
    medHiePres = models.CharField(max_length=30)
    dosisHiePres = models.IntegerField()
    viaAdmPres = models.CharField(max_length=10)
    viaAdmHiePres = models.CharField(max_length=10)

    def __str__(self):
        return self.nomNefro

class admiAnemia(models.Model):
    presAnemia = models.ForeignKey(presAnemia, on_delete=models.CASCADE)
    fechaAdmi = models.DateField()
    nomEnfer = models.CharField(max_length=30)
    medAdmi = models.CharField(max_length=30)
    dosisAdmi = models.IntegerField()
    medHieAdmi = models.CharField(max_length=30)
    dosisHieAdmi = models.IntegerField()
    viaAdm = models.CharField(max_length=10)
    viaAdmHierro = models.CharField(max_length=10)

    def __str__(self):
        return self.nomEnfer