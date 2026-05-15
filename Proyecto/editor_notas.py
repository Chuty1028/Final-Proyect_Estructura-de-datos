from stacks import Stack


# clase que representa una accion realizada en el editor
# cada vez que el usuario escribe o borra algo se crea una accion
class Accion:

    # constructor de la accion
    def __init__(self, tipo, antes, despues):

        # tipo de accion (escribir o eliminar)
        self.tipo = tipo

        # estado del texto antes de la accion (hol)
        self.antes = antes

        # estado del texto despues de la accion (hola)
        self.despues = despues
# undo y redo se basan en antes y despues


# clase principal del editor de notas
class EditorNotas:

    # constructor del editor
    def __init__(self):

        # texto actual del editor
        self.texto = ""

        # stack principal donde se guardan las acciones realizadas (Este historial actua como UNDO)
        self.historial = Stack()

        # stack secundaria donde se guardan las acciones deshechas (sirve para REDO)
        self.redo = Stack()

    
    # --- FUNCIONALIDAD 1 / escribir texto --- 
    
    def escribir(self, contenido):

        # si el texto esta vacio no hace nada pero sirve como seguridad. APP.py igual siempre revisa.
        if contenido == "":
            return

        # self.texto es lo que habia y contenido es el nuevo texto que viene
        nuevo_texto = self.texto + contenido

        # crea una accion con:
        # tipo de accion
        # texto antes del cambio
        # texto despues del cambio
        accion = Accion("escribir", self.texto, nuevo_texto)
        #este objeto es el que permite deshacer porque guardo que ahbia antes y que hay despues

        # guarda la accion en la stack historial (encima de la pila)
        self.historial.push(accion)

        # limpia redo porque se hizo una nueva accion
        self.redo.limpiar()
        # limpia redo porque si el usuario escribe algo nuevo despues de un undo
        # los caminos viejos del redo ya no tienen sentido, el historial tomo un camino nuevo

        # actualiza el texto del editor
        self.texto = nuevo_texto



    # --- FUNCIONALIDAD CORE 2 / eliminar texto --- 
    # (cantidad = cuantas letras se borran)
    def eliminar(self, cantidad):

        # si la cantidad es invalida sale del metodo
        if cantidad <= 0:
            return

        # si quiere borrar mas letras de las que hay
        # el editor queda vacio
        if cantidad > len(self.texto):
            nuevo_texto = ""

        # elimina la cantidad indicada de caracteres
        else:
            nuevo_texto = self.texto[:-cantidad]

        # crea la accion de eliminar
        accion = Accion("eliminar", self.texto, nuevo_texto)

        # guarda la accion en historial para poder hacer undo despues
        self.historial.push(accion)

        # limpia redo porque existe una nueva accion
        self.redo.limpiar()

        # actualiza el texto
        self.texto = nuevo_texto
 
 
    # --- FUNCIONALIDAD CORE 3 / deshacer accion --- 

    def deshacer(self):

        # verifica si historial esta vacio
        if self.historial.esta_vacia():
            return False

        # elimina la ultima accion realizada
        accion = self.historial.pop()

        # mueve la accion a la stack redo
        self.redo.push(accion)

        # restaura el texto anterior
        self.texto = accion.antes

        return True


    # --- FUNCIONALIDAD CORE 4 rehacer accion --- 
    
    def rehacer(self):

        # verifica si redo esta vacio
        if self.redo.esta_vacia():
            return False

        # obtiene la ultima accion deshecha
        accion = self.redo.pop()

        # vuelve a guardar la accion en historial
        self.historial.push(accion)

        # restaura el texto despues de la accion
        self.texto = accion.despues

        return True
    

    # --- FUNCIONALIDAD CORE 5 / limpiar editor --- 

    def limpiar_editor(self):

        # elimina todo el texto
        self.texto = ""

        # limpia historial
        self.historial.limpiar()

        # limpia redo
        self.redo.limpiar()

