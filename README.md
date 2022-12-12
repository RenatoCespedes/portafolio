
# Portafolio
La idea de este proyecto es que cada persona tenga su propio portafolio.

## Funcionalidades
* Una vez que la persona ingresa al sistema, se valida el usuario y la contraseña. 
* El usuario logueado no puede acceder a otros portafolios que no sean el suyo, es decir si intenta ingresar al portafolio de otra persona, solo se devuelve la pagina del portafolio del usuario logueado.
* El sistema cuenta con registro de proyectos, en el cual cada persona registra un proyecto propio. En este se pedira el titulo del proyecto, descripción, tags, imagen,url del repositorio.
* El perfil muestra todos los proyectos que tenga la persona hasta el momento.
* Se puede ver mas a detalle sobre el proyecto si se hace click en la imagen.
* Se puede realizar una edición de los campos del proyecto.

# INSTALACION
Pasos para la ejecución del archivo
--
- Clonar el repositorio 
```bash
  git clone url_github
```
- Instalar las librerias del requirements

```bash
  pip install -r requirements.txt
```
- Una vez instalado cambiar algunos campos de portafolio/settings con tu entorno local

```bash
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': '#####',
        'USER': '#####',
        'PASSWORD': '#####',
        'HOST':'#####',
        'PORT':'#####'
    }
}
```

- Despues ejecutar el servicio 
```bash
  python manage.py runserver
```






