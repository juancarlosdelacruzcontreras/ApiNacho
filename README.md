<div align="center"><img src="https://www.brandbucket.com/sites/default/files/logo_uploads/334406/large_devmonks.png"></div>

<div align="center">
  
  <a href="https://pypi.org/project/httpx/">
  <img src="https://img.shields.io/github/pipenv/locked/dependency-version/juancarlosdelacruzcontreras/ApiNacho/httpx/main?color=orange">
  </a>
  
  <a href="https://pypi.org/project/requests/">
  <img src="https://img.shields.io/github/pipenv/locked/dependency-version/juancarlosdelacruzcontreras/ApiNacho/requests/main?color=orange">
  </a>
  
  <a href="https://pypi.org/project/tabulate/">
  <img src="https://img.shields.io/github/pipenv/locked/dependency-version/juancarlosdelacruzcontreras/ApiNacho/tabulate/main?color=orange">
  </a>
  
  <a href="https://pypi.org/project/progress/">
  <img src="https://img.shields.io/github/pipenv/locked/dependency-version/juancarlosdelacruzcontreras/ApiNacho/progress/main?color=orange">
  </a>
  
  <a href="https://pypi.org/project/colorama/">
  <img src="https://img.shields.io/github/pipenv/locked/dependency-version/juancarlosdelacruzcontreras/ApiNacho/colorama/main?color=orange">
  </a>
</div>

<div align="center">
  
  <a href="https://github.com/juancarlosdelacruzcontreras/ApiNacho/issues">
  <img src="https://img.shields.io/github/issues/juancarlosdelacruzcontreras/ApiNacho">
  </a>
  
  <a href="https://github.com/juancarlosdelacruzcontreras/ApiNacho/pulls">
  <img src="https://img.shields.io/github/issues-pr-closed/juancarlosdelacruzcontreras/ApiNacho">
  </a>
  
</div>

***
# **Direcciones IPv4 e IPv6 públicas**

Podrá indicar direcciones IPv4 o IPV6 públicas usando a elección el consumo de alguna API de los siguientes proveedore: . 
https://ipstack.com/ o https://ipapi.co/

Obtendrá la información en formatos JSON, la tabulará y agregará colores para una mejor apariencia. 

  1. Desarrollado con Python como lenguaje de programación, empleando entornos virtuales.
  2. El software debe gestionar excepciones, impidiendo la detención abrupta del script.
  3. Emplear clases y módulos.
  4. Todos los scripts deben ser documentados por:
    Autor, fecha de creación, última modificación, descripción de funciones.
  5. El código final debe ser concentrado en un repositorio de GitHub y compartido con el profesor. Se sugiere que empleen ramas para cada colaborador. El historial será analizado para verificar sus aportaciones, en git usen nick-names o cuentas que permitan su correcta identificación.

## Datos generales / Distribución considerada.
  
  * 2 – API 1 – Ipv4 – Ipv6.
  * 2 – API 2 – Ipv4 – Ipv6.
  * 1 – Administrar GitHub, mejorar la presentación de la aplicación (tabulares y colores) – generación de video.

## Ejecutar localmente.

Clonar el proyecto

```bash
  git clone https://github.com/juancarlosdelacruzcontreras/ApiNacho
```

## Instalar entorno virtual Pipenv.

Crear entorno virtual ----> (venv), es el nombre del entorno creado:

```bash
  python -m venv venv 
```

Instalar el paquete pipenv:

```bash
  pip install pipenv
```

Inicializar un nuevo entorno virtual:

```bash
  pipenv shell
```

Instalar dependencias desde el archivo Pipfile:

```bash
  pipenv install
```

O instalar dependencias con las versiones exactas usadas durante el desarrollo desde el archivo Pipfile.lock:

```bash
  pipenv install --ignore-pipfile
```

Correr la aplicación desde el archivo main.py:

```bash
  python main.py
```

## Otras opciones para usar Pipenv.

Ver dependencias instaladas en el entorno virtual:

```bash
  pipenv lock -r
```

Ver el árbol de las dependencias instaladas en el entorno virtual:

```bash
  pipenv graph
```

Ver entorno virtual creados:

```bash
  pipenv --venv
```

Eliminar entorno virtual:

```bash
  pipenv --rm
```


## Video del uso de la applicación.

[![Alt text](https://img.youtube.com/vi/S1o8wkBgEeU/0.jpg)](https://www.youtube.com/watch?v=S1o8wkBgEeU)


Por hacer "To do":
* ✅ Documentación.
*  ✅ PMenú inicio.

* ✅ API 1
    * ✅ IPv4
    * ✅ IPv6

* ✅ API 2
    * ✅ IPv4
    * ✅ IPv6

* ✅ Testear
    * ✅ IPI 1
    * ✅ IPI 2

* ✅ Video
    * ✅ IPv4 & IPv6 - API 1
    * ✅ IPv6 & IPv6 - API 2
