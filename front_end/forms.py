from django.forms import ModelForm
from front_end.models import Especies

# Create the form class.
class Especiesform(ModelForm):
    class Meta:
        model = Especies
        fields = ['Classe', 'Ordem', 'Familia', 'Genero', 'Especie', 'Nome_popular', 'Data_da_coleta',
                  'Hora_da_coleta', 'Datum', 'Coordenada_x', 'Coordenada_y', 'Metodo_de_coleta', 'Tipo_de_registro', 'Responsavel_pela_coleta']

