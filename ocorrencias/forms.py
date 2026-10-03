from django import forms
from .models import Ocorrencia


class OcorrenciaForm(forms.ModelForm):
    foto_upload = forms.ImageField(
        required=False,
        label='Foto'
    )

    class Meta:
        model = Ocorrencia
        fields = [
            'local',
            'categoria',
            'descricao',
            'prioridade',
        ]


class EditarOcorrenciaForm(forms.ModelForm):
    foto_upload = forms.ImageField(
        required=False,
        label='Nova foto'
    )

    class Meta:
        model = Ocorrencia
        fields = [
            'local',
            'categoria',
            'descricao',
            'prioridade',
            'status',
        ]