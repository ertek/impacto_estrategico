# Monitor de sitios - Impacto Estratégico

Sistema de monitoreo de sitios web, desarrollado en Python con el framwork Django.

## Iniciar con vagrant (recomendado)

Requisitos del sistema:

* Vagrant [https://www.vagrantup.com/intro/getting-started/index.html]()
* VirutalBox [https://www.virtualbox.org/]()

Una vez instalados los requisitos ejecutar lo siguiente:

```bash
git clone http://github.com/ertek/impacto_estrategico.git
cd impacto_estrategico
vagrant up
```

La instancia correrá en la siguiente direccion:

[http://192.168.10.10/]()

Para crear el super usuario ejecutar el siguiente comando:

```bash
vagrant ssh
cd /vagrant
python manage.py createsuperuser
```

## Configuración

Requisitos del sistema:

* python2.7+
* pip
* virtualenv

## Instalación manual

```bash
git clone http://github.com/ertek/impacto_estrategico.git
cd impacto_estrategico
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
```

## Iniciar django

```bash
python manage.py runserver
```

## Inicar la instancia de monitoreo

```bash
python monitor.py start
```

## Usando la aplicación de django

Para agregar sitios a la aplicación solo hace falta entrar al administrador y en la aplicación de *Sitios* agregarlos. Permite configurar url, frecuencia de monitoreo y el timeout del request.

Para obtener el los archivos *csv*, se pueden descargar del index de la página, en el link del menú superior.

Para ver las tablas solo hace falta rellenar los campos de la vista principal, haciendo uso de las opciones para filtrado. El único campo requerido es el del archivo *csv*.