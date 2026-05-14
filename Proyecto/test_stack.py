import unittest                          
from Proyecto.stacks import Stack                 

class TestStack(unittest.TestCase):      # hereda de TestCase para tener assertEqual, True, False y None
                                         # dependiendo que hay que probar se usa cada una

    def test_push_y_peek(self):                  # test: verificar que push guarda
        s = Stack()                              # crea una pila vacía
        s.push("alex")
        s.push("Daniel")
        s.push("Joaquin")
        self.assertEqual(s.peek(), "Joaquin")   # ¿el tope es "Joauqin"? si no → falla

    def test_pop_regresa_valor(self):             # test: verificar que pop devuelve el valor correcto
        s = Stack()
        s.push("Daniel")                              
        self.assertEqual(s.pop(), "Daniel")            # ¿pop devuelve "Daniel"? si no → falla

    def test_pop_vacia(self):                # test: verificar que pop en pila vacía no truena
        s = Stack()                         
        self.assertIsNone(s.pop())           # ¿pop devuelve None? si no → falla

    def test_esta_vacia_true(self):      # test: verificar que una pila nueva está vacía
        s = Stack()                      
        self.assertTrue(s.esta_vacia())  # ¿esta_vacia() es True? si no → falla

    def test_esta_vacia_false(self):          # test: verificar que con un elemento ya no está vacía
        s = Stack()                           
        s.push("no esta vacia")
        self.assertFalse(s.esta_vacia())      # ¿esta_vacia() es False? si no → falla

    def test_tamanio(self):              # test: verificar que el contador cuenta bien
        s = Stack()                     
        s.push("a")                      
        s.push("b")                      
        self.assertEqual(s.tamanio, 2)   # ¿tamano es 2? si no → falla

    def test_limpiar(self):              # test: verificar que limpiar borra todo
        s = Stack()                      # crea una pila vacía
        s.push("a")                      # mete "a"
        s.push("b")                      # mete "b"
        s.limpiar()                      # limpia la pila
        self.assertTrue(s.esta_vacia())  # ¿quedó vacía? si no → falla
        self.assertEqual(s.tamanio, 0)   # ¿el contador volvió a 0? si no → falla

    def test_orden_LIFO(self):           # test: verificar que el último en entrar es el primero en salir
        s = Stack()                      # crea una pila vacía
        s.push("primero")                     
        s.push("segundo")                       
        self.assertEqual(s.pop(), "segundo")  # ¿pop devuelve "segundo"? si no → falla

    def test_a_lista(self):              # test: verificar que la conversión a lista es correcta
        s = Stack()                      # crea una pila vacía
        s.push("a")
        s.push("b")
        self.assertEqual(s.lista(), ["b", "a"])  # ¿la lista es ["b","a"] (de arriba a abajo)? si no → falla

    def test_peek_valor(self):           # test: verificar que peek devuelve el valor del tope
        s = Stack()                      # crea una pila vacía
        s.push("Perro")                   # mete "Perro"
        self.assertEqual(s.peek(), "Perro")  # ¿peek devuelve "Perro"? si no → falla

