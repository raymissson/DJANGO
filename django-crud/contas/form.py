from django.forms import ModelForm
from .models import Transacao

class TranscaoForm(ModelForm):
    class Meta:
        model = Transacao
        fields = ['data','descricao', 'valor', 'observacoes', 'categoria']