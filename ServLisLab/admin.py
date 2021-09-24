from django.contrib import admin

from ServLisLab.models import Solexalab,Solexalabcps
# Register your models here.

class SolexalabAdmin(admin.ModelAdmin):
    list_display = ('soleqporicenasicod', 'soleqpcenasicod', 'soleqptipexacod', 'soleqpexanum', 'soleqpproeqlcod', 'soleqpsolexafec', 
                    'soleqpordcod', 'soleqptipdocidenpercod', 'soleqpperasisdociden', 'soleqpprocolcod', 'soleqpproapepat', 'soleqpproapemat',
                    'soleqpproprinom', 'soleqpprosegnom', 'soleqppactipdocidencod', 'soleqppacdocidennum', 'soleqppacapepat', 'soleqppacapemat', 'soleqppacprinom',
                    'soleqppacsegnom', 'soleqppachisclinum', 'soleqppacautcod', 'soleqppacsexcod', 'soleqppacnacfec', 'soleqppacedad', 'soleqppacestcivcod', 
                    'soleqppactelfij', 'soleqppactelcel', 'soleqparehoscod', 'soleqppacfamtel', 'soleqpserhoscod', 'soleqpemecod', 'soleqptopemecod', 
                    'soleqpestenfcod', 'soleqphabcod', 'soleqpcamcod', 'soleqpcenquicod', 'soleqpsalopecod', 'soleqpsiscod', 'soleqpdirip', 
                    'soleqpusucrecod', 'soleqpcrefec', 'solflgexito', 'solflgtransferencia')
    search_fields = ('soleqppacdocidennum',)

class SolexalabcpsAdmin(admin.ModelAdmin):
    list_display = ('soleqpcenasicod', 'soleqptipexacod', 'soleqpexanum', 'soleqpcpscod', 'soleqpmuecod', 
                    'soleqpsedexacod', 'soleqpareexacod', 'reseqptomafec', 'reseqptomahor', 'soleqpprovcod', 'soleqpflgtranseqp')
    search_fields = ('soleqpexanum',)

admin.site.register(Solexalab, SolexalabAdmin)
admin.site.register(Solexalabcps, SolexalabcpsAdmin)
