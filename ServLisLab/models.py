# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models

class Solexalab(models.Model):
    soleqporicenasicod = models.CharField(db_column='SolEqpOriCenAsiCod', max_length=1)  # Field name made lowercase.
    soleqpcenasicod = models.CharField(db_column='SolEqpCenAsiCod', max_length=3)  # Field name made lowercase.
    soleqptipexacod = models.CharField(db_column='SolEqpTipExaCod', max_length=1)  # Field name made lowercase.
    soleqpexanum = models.DecimalField(db_column='SolEqpExaNum', primary_key=True, max_digits=10, decimal_places=0)  # Field name made lowercase.
    soleqpproeqlcod = models.CharField(db_column='SolEqpProEqLCod', max_length=2, blank=True, null=True)  # Field name made lowercase.
    soleqpsolexafec = models.CharField(db_column='SolEqpSolExaFec', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soleqpordcod = models.CharField(db_column='SolEqpOrdCod', max_length=8, blank=True, null=True)  # Field name made lowercase.
    soleqptipdocidenpercod = models.CharField(db_column='SolEqpTipDocIdenPerCod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    soleqpperasisdociden = models.CharField(db_column='SolEqpPerAsisDocIden', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soleqpprocolcod = models.CharField(db_column='SolEqpProColCod', max_length=5, blank=True, null=True)  # Field name made lowercase.
    soleqpproapepat = models.CharField(db_column='SolEqpProApePat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    soleqpproapemat = models.CharField(db_column='SolEqpProApeMat', max_length=30, blank=True, null=True)  # Field name made lowercase.
    soleqpproprinom = models.CharField(db_column='SolEqpProPriNom', max_length=20, blank=True, null=True)  # Field name made lowercase.
    soleqpprosegnom = models.CharField(db_column='SolEqpProSegNom', max_length=20, blank=True, null=True)  # Field name made lowercase.
    soleqppactipdocidencod = models.CharField(db_column='SolEqpPacTipDocIdenCod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    soleqppacdocidennum = models.CharField(db_column='SolEqpPacDocIdenNum', max_length=15, blank=True, null=True)  # Field name made lowercase.
    soleqppacapepat = models.CharField(db_column='SolEqpPacApePat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    soleqppacapemat = models.CharField(db_column='SolEqpPacApeMat', max_length=20, blank=True, null=True)  # Field name made lowercase.
    soleqppacprinom = models.CharField(db_column='SolEqpPacPriNom', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soleqppacsegnom = models.CharField(db_column='SolEqpPacSegNom', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soleqppachisclinum = models.DecimalField(db_column='SolEqpPacHisCliNum', max_digits=10, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    soleqppacautcod = models.CharField(db_column='SolEqpPacAutCod', max_length=15, blank=True, null=True)  # Field name made lowercase.
    soleqppacsexcod = models.CharField(db_column='SolEqpPacSexCod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    soleqppacnacfec = models.CharField(db_column='SolEqpPacNacFec', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soleqppacedad = models.DecimalField(db_column='SolEqpPacEdad', max_digits=3, decimal_places=0, blank=True, null=True)  # Field name made lowercase.
    soleqppacestcivcod = models.CharField(db_column='SolEqpPacEstCivCod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    soleqppactelfij = models.CharField(db_column='SolEqpPacTelFij', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soleqppactelcel = models.CharField(db_column='SolEqpPacTelCel', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soleqppacfamtel = models.CharField(db_column='SolEqpPacFamTel', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soleqparehoscod = models.CharField(db_column='SolEqpAreHosCod', max_length=2, blank=True, null=True)  # Field name made lowercase.
    soleqpserhoscod = models.CharField(db_column='SolEqpSerHosCod', max_length=3, blank=True, null=True)  # Field name made lowercase.
    soleqpemecod = models.CharField(db_column='SolEqpEmeCod', max_length=2, blank=True, null=True)  # Field name made lowercase.
    soleqptopemecod = models.CharField(db_column='SolEqpTopEmeCod', max_length=2, blank=True, null=True)  # Field name made lowercase.
    soleqpestenfcod = models.CharField(db_column='SolEqpEstEnfCod', max_length=2, blank=True, null=True)  # Field name made lowercase.
    soleqphabcod = models.CharField(db_column='SolEqpHabCod', max_length=4, blank=True, null=True)  # Field name made lowercase.
    soleqpcamcod = models.CharField(db_column='SolEqpCamCod', max_length=5, blank=True, null=True)  # Field name made lowercase.
    soleqpcenquicod = models.CharField(db_column='SolEqpCenQuiCod', max_length=2, blank=True, null=True)  # Field name made lowercase.
    soleqpsalopecod = models.CharField(db_column='SolEqpSalOpeCod', max_length=2, blank=True, null=True)  # Field name made lowercase.
    soleqpsiscod = models.CharField(db_column='SolEqpSisCod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    soleqpdirip = models.CharField(db_column='SolEqpDirIp', max_length=15, blank=True, null=True)  # Field name made lowercase.
    soleqpusucrecod = models.CharField(db_column='SolEqpUsuCreCod', max_length=10, blank=True, null=True)  # Field name made lowercase.
    soleqpcrefec = models.CharField(db_column='SolEqpCreFec', max_length=20, blank=True, null=True)  # Field name made lowercase.
    solflgexito = models.CharField(db_column='SolFlgExito', max_length=1, blank=True, null=True)  # Field name made lowercase.
    solflgtransferencia = models.CharField(db_column='SolFlgTransferencia', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolExaLab'
        unique_together = (('soleqporicenasicod', 'soleqpcenasicod', 'soleqptipexacod', 'soleqpexanum'),)

class Solexalabcps(models.Model):
    soleqporicenasicod = models.CharField(db_column='SolEqpOriCenAsiCod', max_length=1)  # Field name made lowercase.
    soleqpcenasicod = models.CharField(db_column='SolEqpCenAsiCod', max_length=3)  # Field name made lowercase.
    soleqptipexacod = models.CharField(db_column='SolEqpTipExaCod', max_length=1)  # Field name made lowercase.
    soleqpexanum = models.OneToOneField(Solexalab, models.DO_NOTHING, db_column='SolEqpExaNum', primary_key=True)  # Field name made lowercase.
    soleqpcpscod = models.CharField(db_column='SolEqpCPSCod', max_length=5)  # Field name made lowercase.
    soleqpmuecod = models.CharField(db_column='SolEqpMueCod', max_length=3)  # Field name made lowercase.
    soleqpsedexacod = models.CharField(db_column='SolEqpSedExaCod', max_length=2, blank=True, null=True)  # Field name made lowercase.
    soleqpareexacod = models.CharField(db_column='SolEqpAreExaCod', max_length=1, blank=True, null=True)  # Field name made lowercase.
    reseqptomafec = models.CharField(db_column='ResEqpTomaFec', max_length=10, blank=True, null=True)  # Field name made lowercase.
    reseqptomahor = models.CharField(db_column='ResEqpTomaHor', max_length=8, blank=True, null=True)  # Field name made lowercase.
    soleqpprovcod = models.CharField(db_column='SolEqpProvCod', max_length=2)  # Field name made lowercase.
    soleqpflgtranseqp = models.CharField(db_column='SolEqpFlgTransEqp', max_length=1, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'SolExaLabCPS'
        unique_together = (('soleqporicenasicod', 'soleqpcenasicod', 'soleqptipexacod', 'soleqpexanum', 'soleqpcpscod', 'soleqpmuecod', 'soleqpprovcod'),)

class Pruebadatos(models.Model):
    id = models.IntegerField(primary_key=True)
    dato = models.CharField(max_length=1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pruebaDatos'


