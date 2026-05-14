from editor_notas import EditorNotas


# crea el editor
editor = EditorNotas()


while True:

    print("\n===== EDITOR DE NOTAS =====")

    print("\nTexto actual:")
    print(editor.obtener_texto())

    print("\n1. Escribir texto")
    print("2. Eliminar texto")
    print("3. Undo")
    print("4. Redo")
    print("5. Ver historial")
    print("6. Ver redo")
    print("7. Limpiar editor")
    print("8. Salir")

    opcion = input("\nSeleccione una opcion: ")

    # ESCRIBIR TEXTO
    if opcion == "1":

        contenido = input("Ingrese texto: ")

        editor.escribir(contenido)

        print("Texto agregado.")
        

    # ELIMINAR TEXTO
    elif opcion == "2":

        cantidad = int(input("Cantidad de caracteres a eliminar: "))

        editor.eliminar(cantidad)

        print("Texto eliminado.")


    # UNDO
    elif opcion == "3":

        resultado = editor.deshacer()

        if resultado:
            print("Accion deshecha.")
        else:
            print("No hay acciones para deshacer.")


    # REDO
    elif opcion == "4":

        resultado = editor.rehacer()

        if resultado:
            print("Accion rehecha.")
        else:
            print("No hay acciones para rehacer.")


    # VER HISTORIAL
    elif opcion == "5":

        print("\nHistorial:")
        print(editor.mostrar_historial())


    # VER REDO
    elif opcion == "6":

        print("\nRedo:")
        print(editor.mostrar_redo())


    # LIMPIAR EDITOR
    elif opcion == "7":

        editor.limpiar_editor()

        print("Editor limpiado.")


    # SALIR
    elif opcion == "8":

        print("Saliendo del programa...")

        break

    else:

        print("Opcion invalida.")