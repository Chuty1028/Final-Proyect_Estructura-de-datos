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
