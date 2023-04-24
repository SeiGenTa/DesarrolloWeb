# Ejercicio 3

**Nombre**: Alvaro Enrique Martinez Gonzalez

---

## Pregunta 1

Usted cuenta con el siguiente proyecto de flask:
```bash
flask_app
├── app.py
├── static
│   ├── css
│   │   └── styles.css
│   ├── js
│   │   └── code.js
│   └── svg
│       └── icon.svg
└── templates
    ├── base.html
    └── ruta.html
```
En donde `app.py` tiene las siguientes rutas:
```python
@app.route("/", methods=["GET"])
def index():
    return render_template("ruta.html")

@app.route("/<num>", methods=["GET"])
def index_param(num):
    return render_template("ruta.html", num=int(num))
```
Y `base.html` tiene la siguiente forma:
```html
<!DOCTYPE html>
<html lang="es">
  <head>
    <meta charset="utf-8" />
    <title>{% block title %}{% endblock %}</title>
    {% block css %}{% endblock %}
  </head>
  <body>
    {% block content %}{% endblock %}
    {% block javascript %}{% endblock %}
  </body>
</html>
```

El objetivo de esta pregunta es que usted rellene los bloques de la template `ruta.html` **utilizando funcionalidades de `Jinja`** tal que se cumplan los siguientes requerimientos:

1. Se enlaza al documento HTML el archivo `styles.css`
2. Se incluye el codigo javascript en `code.js`.
3. En caso de que se entregue una variable `num` en el url, se debera mostrar `num` veces la imagen `icon.svg`.

**Respuesta:**

```html
{% extends 'base.html' %}

{% block title %}Ruta{% endblock %}

{% block css %}
    <link rel="stylesheet" href="{{ url_for('static', filename='css/styles.css')}}">
{% endblock %}

{% block content %}
    <h1>RUTA!</h1>
    <!-- PROGRAME AQUI! -->
    {%if mul %}
      {%for i in range(mul)%}
          <img id="{{ url_for('static', filename='svg/icon.svg')}">
      {%endfor%}
    {%endif}
    {%else%}
      <img id="{{ url_for('static', filename='svg/icon.svg')}">
    {%endelse%}

{% endblock %}

{% block javascript %}
    <script src="{{ url_for('static', filename='js/code.js')}}"></script>
{% endblock %}
```
**Hint:** para ubicar archivos use la funcion `url_for` de `Jinja`.

## Pregunta 2
Usted está haciendo una aplicación Flask y su archivo de rutas se ve así:

```python
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/exito')
def exito():
  return "Respondiste correctamente!"

@app.route('/malo')
def malo():
  return "Respondiste mal :o"

@app.route('/pregunta', method=('GET', 'POST'))
def pregunta():
  return render_template('pregunta.html')
```

En este momento la aplicación envía el HTML *pregunta.html* con un formulario como el siguiente:

```html
<form action="pregunta" method="post" enctype="multipart/form-data">
  <label for="pregunta">Pregunta</label>
  <input id="mi-input" name="pregunta" type="text">
  <button type="submit">Enviar</button>
</form>
```

Complete la función `pregunta` para que al enviar el formulario valide que el texto enviado en el formulario:
- Tenga la palabra "abracadabra"
- Tenga al menos 5 caracteres y máximo 30
- Tenga algún dígito

Si cumple todas estas condiciones redireccione al usuario a la ruta `exito`, de lo contrario redirija a la ruta `malo`. Sólo puede programar en Python en el espacio que se proporciona en la respuesta.

Reciba el formulario si el método es `POST`, tome el input, escriba y use la función `validar_input` para validar el input.

**Respuesta**:

```python
# IMPORTE LO QUE TENGA QUE IMPORTAR DE FLASK
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/exito')
def exito():
  return "Respondiste correctamente!"

@app.route('/malo')
def malo():
  return "Respondiste mal :o"

def validar_input(input):
  if len(input) < 5 or len(input) > 30:
    return False
  if not ("abracadabra" in input):
    return False
  for i in input:
    try:
      int(i)
      return True
    except:
      pass
  return false

@app.route('/pregunta', method=('GET', 'POST'))
def pregunta():
  if request.method == "POST":
    cont_text = request.form.get("pregunta")
    if validar_input(cont_text): return render_template('exito')
    else: return render_template('malo')
  elif request.method == "GET": return render_template('pregunta.html')
```

## Pregunta 3
En auxiliar hemos hablado sobre cómo el input del usuario puede ser malicioso. Un ejemplo de esto son las inyecciones SQL, una de las vulnerabilidades más populares. Ésta consiste en que input hecho por el usuario permite inyectar código en las sentencias SQL que usamos (cómo cuando guardamos algo en la base de datos).

A pesar de ser una de las vulnerabilidades más recurrentes en aplicaciones web, no es la única donde el input del usuario juega una mala pasada. Otro ejemplo es el llamado **Server Side Template Injection** (SSTI). Investigue y explique brevemente en qué consiste esta vulnerabilidad.

**Respuesta**: Este tipo de vulnerabilidad ocurre en aplicaciones web que utilizan plantillas desde el lado del servidor para contruir paginas web dinamicas. Consiste en la manipulacion de variables en una de las platillas, lo que puede provocar que se ejecuten comandos de manera malisioso. Por ejemplo, supongamos que tengamos un form, suponiendo que este no posea una validacion, podriamos colocar un comando {{7*"7"}} lo que haria que cierta parte de la pagina no respondiera como deberia. En particular estas ejemplo es con aplicaciones que utilizan jinja para modificar los html.