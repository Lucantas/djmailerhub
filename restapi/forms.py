from django import forms
from .models import MailConf

class MailConfForm(forms.ModelForm):
    class Meta:
        model = MailConf
        exclude = ['last_login', 'is_superuser', 'groups', 'user_permissions', 'first_name', 'last_name', 'email']
        # password = forms.CharField(
        #     required=False,
        #     widget=forms.PasswordInput(attrs={ 'required': 'false' }),
        # )