from django.db.models import Q
from covid19.models import *
from covid19.serializers import *

#exec(open('imprised_teste_script.py').read())

municipio = Municipio.objects.filter(Q(uf__id=15) & Q(id=1501402))
serializer = MunicipioSerializer(municipio,many=True)
print(serializer.data)
print(list(municipio.values(
                    'uf__id',
                    'uf__nome',
                    'id',
                    'nome',
                    'populacao_total',
                    'populacao_projetada',
                    ))[0])


