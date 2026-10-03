from django import forms
from .models import Ocorrencia


class OcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = [
            'local',
            'categoria',
            'descricao',
            'prioridade',
            'foto',
        ]


class EditarOcorrenciaForm(forms.ModelForm):
    class Meta:
        model = Ocorrencia
        fields = [
            'local',
            'categoria',
            'descricao',
            'prioridade',
            'status',
            'foto',
        ]