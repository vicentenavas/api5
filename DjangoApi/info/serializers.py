from rest_framework import serializers

from .models import Servizio, Socio, Descrizione, Img, SiOcuppa

class DescrizioneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descrizione
        fields = ('descrizioneId','descrizione',)

class ServizioSerializer(serializers.ModelSerializer):
    descrizioni = serializers.SerializerMethodField()

    def get_descrizioni(self, obj):
        descrizioni = obj.descrizioni.all()
        return [{'id': descrizione.id, 'descrizione': descrizione.descrizione} for descrizione in descrizioni]
        

    class Meta:
        model = Servizio
        fields = ('servizioId', 'nome', 'descrizioni', 'imgUrl', 'siOcuppa')

class SocioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Socio
        fields=('socioId', 'nome', 'info')
