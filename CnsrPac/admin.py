from django.contrib import admin

# Register your models here.

from CnsrPac.models import paciente,presAnemia,admiAnemia,exclusionAnemia

class pacienteAdmin(admin.ModelAdmin):
    list_display = ('tipoDoc','numDoc','apePat','apeMat','nombres','fechaNac','sexo','estado')
    search_fields = ('numDoc',)

class presAnemiaAdmin(admin.ModelAdmin):
    list_display = ('paciente','fechaPres','nomNefro','medPres','dosisPres','medHiePres','dosisHiePres','viaAdmPres','viaAdmHiePres')
    search_fields = ('nomNefro',)

class admiAnemiaAdmin(admin.ModelAdmin):
    list_display = ('presAnemia','fechaAdmi','nomEnfer','medAdmi','dosisAdmi','medHieAdmi','dosisHieAdmi','viaAdm','viaAdmHierro')
    search_fields = ('nomEnfer',)

class exclusionAnemiaAdmin(admin.ModelAdmin):
    list_display = ('paciente','fechaExclu','razonExclu','ObservaExclu')
    search_fields = ('razonExclu',)

admin.site.register(paciente, pacienteAdmin)
admin.site.register(presAnemia, presAnemiaAdmin)
admin.site.register(admiAnemia, admiAnemiaAdmin)
admin.site.register(exclusionAnemia, exclusionAnemiaAdmin)