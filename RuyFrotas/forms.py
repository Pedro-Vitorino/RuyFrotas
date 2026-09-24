from django import forms
from .models import Usuario, Motorista, Veiculo, Rota, Solicitacao, Manutencao, Gasto, Viagem

class FormsUsuario(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = "__all__"

class FormsMotorista(forms.ModelForm):
    class Meta:
        model = Motorista
        fields = "__all__"

class FormsVeiculo(forms.ModelForm): 
    class Meta:
        model = Veiculo
        fields = "__all__"

class FormsRota(forms.ModelForm):
    class Meta:
        model = Rota
        fields = "__all__"

class FormsSolicitacao(forms.ModelForm):
    class Meta:
        model = Solicitacao
        fields = "__all__"

class FormsManutencao(forms.ModelForm):
    class Meta:
        model = Manutencao
        fields = "__all__"

class FormsGasto(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = "__all__"

class FormsViagem(forms.ModelForm):
    class Meta:
        model = Viagem
        fields = "__all__"