from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from info.models import Servizio, Socio
from info.serializers import ServizioSerializer, SocioSerializer 
# Create your views here.
def servizioApi(request):
    servizi = Servizio.objects.prefetch_related('descrizioni').all()
    data = []

    for servizio in servizi:
        descrizioni = servizio.descrizioni.all()
        descrizioni_list = [
            {'id': index, 'descrizione': descrizione.descrizione}
            for index, descrizione in enumerate(descrizioni)
        ]

        servizio_data = {
            'servizioId': servizio.servizioId,
            'nome': servizio.nome,
            'descrizioni': descrizioni_list,
            'imgUrl': servizio.imgUrl,
            'siOcuppa': servizio.siOcuppa
        }

        data.append(servizio_data)

    return JsonResponse(data, safe=False)




@csrf_exempt
def socioApi(request, id=0):
    if request.methodd=='GET': 
        socio = Socio.objects.all()
        socio_serializer = SocioSerializer(socio, many=True)
        return JsonResponse(socio_serializer.data, safe=True)