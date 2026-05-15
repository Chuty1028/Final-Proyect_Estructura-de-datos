# test_stack.py — Correr las pruebas

## Comando para correr
Entrar a la carpeta Proyecto y ejecutar:
```
cd Proyecto
python -m unittest test_stack.py -v
```

## Qué significa cada parte
- `python -m unittest` — le dice a Python que corra el módulo de pruebas
- `test_stack.py` — el archivo con los tests
- `-v` — modo detallado, muestra cada test con su resultado (OK o FAIL)

## Resultado esperado
```
test_a_lista ... ok
test_esta_vacia_false ... ok
test_esta_vacia_true ... ok
test_limpiar ... ok
test_orden_LIFO ... ok
test_peek_valor ... ok
test_pop_regresa_valor ... ok
test_pop_vacia ... ok
test_push_y_peek ... ok
test_tamanio ... ok

Ran 10 tests in 0.001s
OK
```
