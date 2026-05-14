# Editor de Notas con Doble Stack

# Alexander López - 20250555
# Daniel Piñol - 20250409


## Descripción del Proyecto

Este proyecto consiste en el desarrollo de un editor de notas simple que implementa una estructura de datos de doble stack (doble pila) para manejar las funciones de Undo y Redo.

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

---

# Explicación de la Doble Stack

El proyecto utiliza dos stacks:

| Stack | Función |
|---|---|
| historial | Guarda las acciones realizadas |
| redo | Guarda las acciones deshechas |

---

# Funcionamiento

## Escritura de texto

Cada vez que el usuario escribe texto:
- se crea una acción
- la acción se guarda en la stack historial

---

## Undo

Cuando el usuario utiliza Undo:
- la última acción se elimina de historial
- la acción pasa a la stack redo
- el texto vuelve a su estado anterior

---

## Redo

Cuando el usuario utiliza Redo:
- la acción se elimina de redo
- vuelve a historial
- el texto se restaura

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

# Implementación de la Stack

## Métodos implementados

- `push()`
- `pop()`
- `peek()`
- `esta_vacia()`
- `limpiar()`
- `lista()`

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

## Con unittest

```bash
python3 -m unittest test_stack.py
```

## Con pytest

```bash
pytest test_stack.py
```

---

# Ejecución del Proyecto

## Abrir interfaz gráfica

Abrir el archivo:

```txt
index.html
```

en el navegador.

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

---

---

# Conclusión

Este proyecto permitió aplicar estructuras de datos en un caso práctico mediante el desarrollo de un editor de notas funcional. La implementación de una doble stack permitió manejar correctamente las operaciones Undo y Redo. 