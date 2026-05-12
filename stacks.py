class Nodo:                                  # es como la cajita donde se va a guardar
    def __init__(self, valor):               # constructor del nodo (valor = al numero que entra a la cajita)
        self.valor = valor                   # guarda el dato del nodo
        self.siguiente = None                # puntero al siguiente nodo (empieza en nada)

class Stack:                                 # clase pila implementada con nodos enlazados
    def __init__(self):                      # constructor de la pila
        self.tope = None                     # referencia al nodo en la cima (empieza vacía)
        self.tamanio = 0                     # contador de elementos en la pila

    def push(self, valor):                   # agrega un elemento a la cima
        nodo = Nodo(valor)                   # crea un nuevo nodo con el valor dado
        nodo.siguiente = self.tope           # el nuevo nodo apunta al antiguo tope
        self.tope = nodo                     # el nuevo nodo se convierte en el tope
        self.tamanio += 1                    # incrementa el contador

    def esta_vacia(self):                    # verifica si la pila no tiene elementos
        return self.tope is None             # es vacía cuando el tope no apunta a nada

    def pop(self):                       # elimina y devuelve el elemento del tope
        if self.esta_vacia():            # si la pila está vacía no hay nada que quitar
            return None                      # devuelve None para indicar pila vacía
        valor = self.tope.valor              # guarda el valor del tope para devolverlo
        self.tope = self.tope.siguiente      # el tope pasa a ser el siguiente nodo
        self.tamanio -= 1                    # decrementa el contador
        return valor                         # devuelve el valor que se eliminó

    def peek(self):                          # consulta el tope sin eliminarlo
        if self.esta_vacia():                # si está vacía no hay tope que consultar
            return None                      # devuelve None para indicar pila vacía
        return self.tope.valor               # devuelve el valor del tope

    def esta_vacia(self):                    # verifica si la pila no tiene elementos
        return self.tope is None             # es vacía cuando el tope no apunta a nada

    def limpiar(self):                       # vacía la pila por completo
        self.tope = None                     # elimina la referencia al tope
        self.tamanio = 0                     # reinicia el contador a cero

    def lista(self):                       # convierte la pila en una lista de Python
        resultado = []                       # lista donde se guardarán los valores
        actual = self.tope                   # empieza desde el tope
        while actual:                        # recorre cada nodo hasta el final (Mira si actual es un nodo o es none)
            resultado.append(actual.valor)   # agrega el valor del nodo a la lista
            actual = actual.siguiente        # avanza al siguiente nodo
        return resultado                     # devuelve la lista con todos los valores
