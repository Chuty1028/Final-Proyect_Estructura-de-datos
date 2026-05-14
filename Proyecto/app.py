import os

# Flask es el framework web; request lee datos del cliente; jsonify convierte dict a JSON; send_from_directory sirve archivos estáticos
from flask import Flask, request, jsonify, send_from_directory
from editor_notas import EditorNotas

# ruta absoluta a la carpeta interfaz (está un nivel arriba de Proyecto/)
INTERFAZ_DIR = os.path.join(os.path.dirname(__file__), "..", "interfaz")

# crea la aplicación Flask
app = Flask(__name__)

# crea una instancia del editor (vive mientras el servidor esté corriendo)
editor = EditorNotas()


# ruta principal: cuando el usuario abre http://127.0.0.1:5001 lo lleva al index.html de interfaz/
@app.route("/")
def index():
    return send_from_directory(INTERFAZ_DIR, "index.html")


# sirve los archivos estáticos de la carpeta interfaz/ (style.css, script.js, etc.)
@app.route("/<path:filename>")
def static_files(filename):
    return send_from_directory(INTERFAZ_DIR, filename)


# ruta para actualizar el texto completo del editor (el frontend envía el texto íntegro)
@app.route("/actualizar", methods=["POST"])
def actualizar():
    texto_nuevo = request.json.get("texto", "")   # texto completo que envía el frontend
    texto_anterior = editor.texto                  # texto que tenía antes

    # calcula el delta: qué se agregó o quitó
    if len(texto_nuevo) > len(texto_anterior):
        # se escribió algo nuevo
        agregado = texto_nuevo[len(texto_anterior):]
        editor.escribir(agregado)
    elif len(texto_nuevo) < len(texto_anterior):
        # se eliminaron caracteres
        cantidad = len(texto_anterior) - len(texto_nuevo)
        editor.eliminar(cantidad)
    # si son iguales no hace nada

    return jsonify(estado())


# ruta para escribir texto: recibe un JSON con {"texto": "..."} y lo agrega al editor
@app.route("/escribir", methods=["POST"])
def escribir():
    texto = request.json.get("texto", "")   # extrae el campo "texto" del JSON recibido
    editor.escribir(texto)                  # llama al método escribir del editor
    return jsonify(estado())                # devuelve el estado actual como JSON


# ruta para deshacer la última acción (Ctrl+Z)
@app.route("/undo", methods=["POST"])
def undo():
    editor.deshacer()       # deshace la última acción
    return jsonify(estado())


# ruta para rehacer una acción deshecha (Ctrl+Y)
@app.route("/redo", methods=["POST"])
def redo():
    editor.rehacer()        # rehace la última acción deshecha
    return jsonify(estado())


# ruta para limpiar todo el editor
@app.route("/limpiar", methods=["POST"])
def limpiar():
    editor.limpiar_editor()     # borra texto e historial completo
    return jsonify(estado())


# ruta para consultar el estado actual sin modificar nada (GET)
@app.route("/estado")
def get_estado():
    return jsonify(estado())


# función auxiliar que arma el diccionario con el estado actual del editor
def estado():
    return {
        "texto": editor.texto,                      # texto actual del editor
        "undo_size": editor.historial.tamanio,      # cuántas acciones se pueden deshacer
        "redo_size": editor.redo.tamanio,           # cuántas acciones se pueden rehacer
        "undo_historial": editor.mostrar_historial(),   # lista de acciones en historial
        "redo_historial": editor.mostrar_redo(),        # lista de acciones en redo
    }


# solo ejecuta el servidor si se corre este archivo directamente (no si se importa)
if __name__ == "__main__":
    app.run(debug=True, port=5001)     # debug=True recarga automáticamente al guardar cambios
