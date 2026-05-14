# Editor de Notas con Doble Stack

# Alexander López - 20250555
# Daniel Piñol - 20250409

---

# Descripción del Proyecto

Este proyecto consiste en el desarrollo de un editor de notas simple que implementa una estructura de datos de doble stack (doble pila) para manejar las funciones de Undo y Redo.

El sistema permite:
- escribir texto
- eliminar texto
- deshacer acciones
- rehacer acciones
- limpiar el editor

---

# Tecnologías Utilizadas

- Python
- HTML
- CSS
- JavaScript
- unittest
- pytest

---

# Estructura del Proyecto

```txt
Final-Proyect_Estructura-de-datos/
│
├── Documentacion/
│   └── README.md
│
├── interfaz/
│   ├── index.html
│   ├── style.css
│   └── script.js
│
└── Proyecto/
    ├── editor_notas.py
    ├── stacks.py
    ├── main.py
    ├── test_stack.py
    ├── .pytest_cache/
    └── benchmarks/
```

---

# Explicación de la Doble Stack

El proyecto utiliza dos stacks:

| Stack | Función |
|---|---|
| historial | Guarda las acciones realizadas |
| redo | Guarda las acciones deshechas |

La doble stack permite mover acciones entre ambas pilas para implementar las operaciones Undo y Redo.

---

# Funcionamiento del Proyecto

## Escritura de texto

Cada vez que el usuario escribe texto:
1. se crea una acción
2. la acción se guarda en la stack historial
3. la stack redo se limpia

---

## Undo

Cuando el usuario utiliza Undo:
1. la última acción se elimina de historial
2. la acción pasa a la stack redo
3. el texto vuelve a su estado anterior

---

## Redo

Cuando el usuario utiliza Redo:
1. la acción se elimina de redo
2. vuelve a historial
3. el texto se restaura

---

# Funcionalidades Core

## 1. Escribir texto
Permite agregar texto al editor.

## 2. Eliminar texto
Permite eliminar caracteres del editor.

## 3. Undo
Permite deshacer la última acción realizada.

## 4. Redo
Permite rehacer una acción deshecha.

## 5. Limpiar editor
Permite reiniciar completamente el editor y las stacks.

---

# Implementación Propia de la Stack

La estructura Stack fue implementada manualmente utilizando nodos enlazados.

## Métodos implementados

### push(valor)

Agrega un elemento a la cima de la pila.

#### Complejidad temporal
```txt
O(1)
```

Porque únicamente modifica referencias al nodo superior.

---

### pop()

Elimina y devuelve el elemento de la cima.

#### Complejidad temporal
```txt
O(1)
```

Porque solo elimina el nodo superior.

---

### peek()

Devuelve el valor del tope sin eliminarlo.

#### Complejidad temporal
```txt
O(1)
```

---

### esta_vacia()

Verifica si la pila está vacía.

#### Complejidad temporal
```txt
O(1)
```

---

### limpiar()

Vacía completamente la pila.

#### Complejidad temporal
```txt
O(1)
```

Porque elimina la referencia al nodo superior.

---

### lista()

Convierte la pila en una lista de Python.

#### Complejidad temporal
```txt
O(n)
```

Porque recorre todos los nodos de la pila.

---

# Testing

El proyecto incluye pruebas utilizando `unittest`.

## Escenarios testeados

1. Push y Peek
2. Pop devuelve valor correcto
3. Pop en stack vacía
4. Verificar stack vacía
5. Verificar stack no vacía
6. Tamaño de la stack
7. Limpiar stack
8. Orden LIFO
9. Conversión a lista
10. Peek devuelve valor correcto

---

# Ejecutar los Tests

## Entrar a la carpeta del proyecto

```bash
cd Proyecto
```

---

## Ejecutar tests con unittest

```bash
python3 -m unittest test_stack.py
```

---

## Ejecutar tests con pytest

```bash
pytest test_stack.py
```

---

# Clonar el Repositorio

```bash
git clone git@github.com:Chuty1028/Final-Proyect_Estructura-de-datos.git
```

Entrar al proyecto:

```bash
cd Final-Proyect_Estructura-de-datos
```

---

# Ejecución del Proyecto

## Ejecutar versión Python

Entrar a la carpeta:

```bash
cd Proyecto
```

Ejecutar:

```bash
python3 main.py
```

---

## Ejecutar interfaz gráfica (Web)

El frontend está conectado a un servidor Flask en el backend para gestionar las estructuras de datos (Stacks). Para ejecutar la interfaz correctamente:

Entrar a la carpeta del proyecto (si no lo has hecho):

```bash
cd Proyecto
```

Instalar las dependencias requeridas (Flask):

```bash
pip install flask
```

Ejecutar el servidor principal:

```bash
python3 app.py
```

Por último, abrir en tu navegador web la siguiente dirección:

```txt
http://127.0.0.1:5001
```

---

# Interfaz Gráfica

La interfaz fue desarrollada utilizando:
- HTML
- CSS
- JavaScript

Incluye:
- área de escritura
- botón Undo
- botón Redo
- botón Eliminar

La interfaz fue diseñada con un estilo visual inspirado en aplicaciones modernas de notas.

---

# Conclusión

Este proyecto permitió aplicar estructuras de datos en un caso práctico mediante el desarrollo de un editor de notas funcional.

La implementación de una doble stack permitió manejar correctamente las operaciones Undo y Redo, demostrando el uso real de las pilas en aplicaciones modernas.