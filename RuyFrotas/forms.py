from django import forms
from django.forms import inlineformset_factory
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import PasswordChangeForm
from datetime import timedelta

from .models import (
    Usuario,
    Motorista,
    Veiculo,
    Rota,
    Solicitacao,
    Manutencao,
    Gasto,
    Viagem
)


Usuario = get_user_model()


# =========================
# USUÁRIO
# =========================

class FormsUsuario(forms.ModelForm):

    password = forms.CharField(
        label='Senha',
        widget=forms.PasswordInput,
        required=True
    )

    password_confirm = forms.CharField(
        label='Confirmar senha',
        widget=forms.PasswordInput,
        required=True
    )

    class Meta:
        model = Usuario
        fields = [
            'username',
            'email',
            'password',
            'password_confirm',
        ]

    def clean(self):
        cleaned_data = super().clean()

        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')

        if password and password != password_confirm:
            self.add_error(
                'password_confirm',
                'As senhas não coincidem.'
            )

        return cleaned_data

    def save(self, commit=True):
        usuario = super().save(commit=False)

        password = self.cleaned_data.get('password')

        if password:
            usuario.set_password(password)

        usuario.tipo = 'MOTORISTA'

        if commit:
            usuario.save()

        return usuario


# =========================
# MOTORISTA
# =========================

class FormsMotorista(forms.ModelForm):
    class Meta:
        model = Motorista
        exclude = ['usuario']
        widgets = {
            'ingresso': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                }
            ),
        }

class FormsMotoristaAdmin(forms.ModelForm):
    class Meta:
        model = Motorista
        exclude = ['usuario']
        widgets = {
            'ingresso': forms.DateInput(
                format='%Y-%m-%d',
                attrs={
                    'type': 'date',
                }
            ),
        }


MotoristaFormSet = inlineformset_factory(
    Usuario,
    Motorista,
    form=FormsMotorista,
    extra=1,
    max_num=1,
    can_delete=False
)

class FormsSolicitacaoMotorista(forms.ModelForm):
    class Meta:
        model = Solicitacao
        exclude = ['motorista', 'atendida', 'data']
        
# =========================
# MINHA CONTA
# =========================

class FormsMinhaConta(forms.ModelForm):

    class Meta:
        model = Usuario
        fields = ['username', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].label = 'Usuário'
        self.fields['email'].label = 'E-mail'


class FormsAlterarSenha(PasswordChangeForm):

    old_password = forms.CharField(
        label='Senha atual',
        widget=forms.PasswordInput
    )

    new_password1 = forms.CharField(
        label='Nova senha',
        widget=forms.PasswordInput
    )

    new_password2 = forms.CharField(
        label='Confirmar nova senha',
        widget=forms.PasswordInput
    )


# =========================
# VEÍCULO
# =========================

class FormsVeiculo(forms.ModelForm):

    class Meta:
        model = Veiculo
        fields = "__all__"


# =========================
# ROTA
# =========================

class FormsRota(forms.ModelForm):

    horas = forms.IntegerField(
        min_value=0,
        max_value=999,
        initial=0,
        required=True,
        label="Horas",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "00",
            "min": 0,
            "max": 999
        })
    )

    minutos = forms.IntegerField(
        min_value=0,
        max_value=59,
        initial=0,
        required=True,
        label="Minutos",
        widget=forms.NumberInput(attrs={
            "class": "form-control",
            "placeholder": "00",
            "min": 0,
            "max": 59
        })
    )

    class Meta:
        model = Rota
        fields = [
            "nome",
            "motoristas",
            "origem",
            "destino"
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # Recupera a duração ao editar uma rota
        if self.instance and self.instance.pk:
            duracao = self.instance.duracao or timedelta()

            total_horas = duracao.days * 24 + duracao.seconds // 3600
            total_minutos = (duracao.seconds % 3600) // 60

            self.fields["horas"].initial = total_horas
            self.fields["minutos"].initial = total_minutos

    def save(self, commit=True):
        rota = super().save(commit=False)

        horas = self.cleaned_data["horas"]
        minutos = self.cleaned_data["minutos"]

        # Converte horas e minutos para DurationField
        rota.duracao = timedelta(
            hours=horas,
            minutes=minutos
        )

        if commit:
            rota.save()
            self.save_m2m()

        return rota


# =========================
# SOLICITAÇÃO
# =========================

class FormsSolicitacao(forms.ModelForm):

    class Meta:
        model = Solicitacao
        fields = "__all__"


# =========================
# MANUTENÇÃO
# =========================

class FormsManutencao(forms.ModelForm):

    class Meta:
        model = Manutencao
        fields = "__all__"


# =========================
# GASTO
# =========================

class FormsGasto(forms.ModelForm):

    class Meta:
        model = Gasto
        fields = "__all__"


# =========================
# VIAGEM
# =========================

class FormsViagem(forms.ModelForm):

    class Meta:
        model = Viagem
        fields = "__all__"