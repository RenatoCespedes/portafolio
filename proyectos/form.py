from django import forms



class ProjectForm(forms.Form):
    foto= forms.CharField(max_length=800)
    titulo=forms.CharField(max_length=100)
    descripcion=forms.CharField(max_length=1000)
    tags=forms.ImageField()
    repo_url=forms.URLField(max_length=800)