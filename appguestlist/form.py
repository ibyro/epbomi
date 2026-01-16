from django import forms
from .models import Invites

class InviteForm(forms.ModelForm):
    class Meta:
        model = Invites
        fields = ["nom","prenom","telephone","dateinvitation","commune","quartier","invitepar","motifdepresence","communauteorigine"]
        