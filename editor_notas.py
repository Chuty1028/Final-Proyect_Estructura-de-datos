from stacks import Stack


# clase que representa una accion realizada en el editor
class Accion:

    # constructor de la accion
    def __init__(self, tipo, antes, despues):

        # tipo de accion (escribir o eliminar)
        self.tipo = tipo

        # estado del texto antes de la accion
        self.antes = antes

        # estado del texto despues de la accion
        self.despues = despues


# clase principal del editor de notas
class EditorNotas:

    # constructor del editor
    def __init__(self):

        # texto actual del editor
        self.texto = ""

        # stack principal donde se guardan las acciones realizadas
        self.historial = Stack()

        # stack secundaria donde se guardan las acciones deshechas
        self.redo = Stack()

    
    # --- FUNCIONALIDAD CORE 1 / escribir texto --- 
    
    def escribir(self, contenido):

        # si el texto esta vacio no hace nada
        if contenido == "":
            return

        # crea el nuevo texto agregando contenido
        nuevo_texto = self.texto + contenido

        # crea una accion con:
        # tipo de accion
        # texto antes del cambio
        # texto despues del cambio
        accion = Accion(
            "escribir",
            self.texto,
            nuevo_texto
        )

        # guarda la accion en la stack historial
        self.historial.push(accion)

        # limpia redo porque se hizo una nueva accion
        self.redo.limpiar()

        # actualiza el texto del editor
        self.texto = nuevo_texto



    # --- FUNCIONALIDAD CORE 2 / eliminar texto --- 
    
    def eliminar(self, cantidad):

        # si la cantidad es invalida no hace nada
        if cantidad <= 0:
            return

        # si la cantidad supera el tamaño del texto
        # el editor queda vacio
        if cantidad > len(self.texto):
            nuevo_texto = ""

        # elimina la cantidad indicada de caracteres
        else:
            nuevo_texto = self.texto[:-cantidad]

        # crea la accion de eliminar
        accion = Accion(
            "eliminar",
            self.texto,
            nuevo_texto
        )

        # guarda la accion en historial
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

    # devuelve el texto actual
    def obtener_texto(self):
        return self.texto

    # muestra las acciones guardadas en historial
    def mostrar_historial(self):

        # convierte la stack historial en lista
        historial = self.historial.lista()

        acciones = []

        # recorre las acciones guardadas
        for accion in historial:

            # guarda solo el tipo de accion
            acciones.append(accion.tipo)

        return acciones

    # muestra las acciones guardadas en redo
    def mostrar_redo(self):

        # convierte redo en lista
        redo = self.redo.lista()

        acciones = []

        # recorre las acciones guardadas
        for accion in redo:

            # guarda el tipo de accion
            acciones.append(accion.tipo)

        return acciones