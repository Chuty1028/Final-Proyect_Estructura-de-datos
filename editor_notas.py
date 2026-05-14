from stacks import Stack


class Accion:
    def __init__(self, tipo, antes, despues):
        self.tipo = tipo
        self.antes = antes
        self.despues = despues


class EditorNotas:
    def __init__(self):
        self.texto = ""
        self.historial = Stack()
        self.redo = Stack()

    # FUNCIONALIDAD CORE 1
    def escribir(self, contenido):

        if contenido == "":
            return

        nuevo_texto = self.texto + contenido

        accion = Accion(
            "escribir",
            self.texto,
            nuevo_texto
        )

        self.historial.push(accion)

        # limpiar redo porque hay nueva accion
        self.redo.limpiar()

        self.texto = nuevo_texto

    # FUNCIONALIDAD CORE 2
    def eliminar(self, cantidad):

        if cantidad <= 0:
            return

        if cantidad > len(self.texto):
            nuevo_texto = ""
        else:
            nuevo_texto = self.texto[:-cantidad]

        accion = Accion(
            "eliminar",
            self.texto,
            nuevo_texto
        )

        self.historial.push(accion)

        self.redo.limpiar()

        self.texto = nuevo_texto
        
    # FUNCIONALIDAD CORE 3
    def deshacer(self):

        if self.historial.esta_vacia():
            return False

        accion = self.historial.pop()

        self.redo.push(accion)

        self.texto = accion.antes

        return True

    # FUNCIONALIDAD CORE 4
    def rehacer(self):

        if self.redo.esta_vacia():
            return False

        accion = self.redo.pop()

        self.historial.push(accion)

        self.texto = accion.despues

        return True

    # FUNCIONALIDAD CORE 5
    def limpiar_editor(self):

        self.texto = ""

        self.historial.limpiar()

        self.redo.limpiar()

    def obtener_texto(self):
        return self.texto

    def mostrar_historial(self):

        historial = self.historial.lista()

        acciones = []

        for accion in historial:
            acciones.append(accion.tipo)

        return acciones

    def mostrar_redo(self):

        redo = self.redo.lista()

        acciones = []

        for accion in redo:
            acciones.append(accion.tipo)

        return acciones
