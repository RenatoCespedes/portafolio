from django import forms



class ProjectForm(forms.Form):
    titulo=forms.CharField(max_length=100)
    descripcion=forms.CharField(max_length=1000)
    tags= forms.CharField(max_length=800)
    foto=forms.ImageField()
    repo_url=forms.URLField(max_length=800)