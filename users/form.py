from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User



class ContactForm(forms.Form):
    nombre=forms.CharField(max_length=50)
    correo=forms.EmailField()
    tema=forms.CharField(max_length=100)
    mensaje=forms.CharField(max_length=1000)

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    # genero=forms.CharField()
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email",  "password1", "password2"]
        label={
            "username":"Nombre de usuario", 
            "first_name":"Nombre", 
            "last_name":"Apellidos",
            "email":"Correo",  
            "password1":"Contraseña",
            "password2":"Vuelve a repetir la contraseña"
        }

    def save(self, commit=True):
        # self.genero=self.cleaned_data['genero']
        user = super(NewUserForm, self).save(commit=False)
        # aumentar el email
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return 