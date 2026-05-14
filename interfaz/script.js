/**
 * Referencias a los elementos del DOM (Document Object Model)
 * Estos elementos representan la interfaz de usuario definida en el HTML.
 */
const editor = document.getElementById("noteArea");     // Área principal de escritura (textarea)
const undoBtn = document.getElementById("undoBtn");     // Botón para deshacer acciones
const redoBtn = document.getElementById("redoBtn");     // Botón para rehacer acciones
const deleteBtn = document.getElementById("deleteBtn"); // Botón para limpiar el editor

/**
 * Función asíncrona para cargar el estado actual del editor desde el servidor.
 * Realiza una petición GET a la ruta "/estado" y actualiza el valor del textarea
 * con el texto recibido del backend.
 */
async function cargarEstado() {
  const respuesta = await fetch("/estado"); // Solicitud al backend Flask
  const data = await respuesta.json();      // Conversión de la respuesta a JSON
  editor.value = data.texto;                // Actualiza el área de texto en pantalla
}

/**
 * Event Listener para el textarea.
 * Se ejecuta automáticamente cada vez que el usuario escribe o borra algo ("input").
 * Envía el texto completo al servidor mediante una petición POST para mantener 
 * la sincronización entre el frontend y las estructuras de datos (Stacks) en el backend.
 */
editor.addEventListener("input", async () => {
  await fetch("/actualizar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ texto: editor.value }) // Envía el estado actual del texto
  });
});

/**
 * Event Listener para el botón "Undo" (Deshacer).
 * Envía una petición al backend para revertir la última acción usando la Stack de historial,
 * y luego recarga el estado para mostrar el cambio en la interfaz.
 */
undoBtn.addEventListener("click", async () => {
  await fetch("/undo", { method: "POST" });
  await cargarEstado(); // Refresca el área de texto con la versión anterior
});

/**
 * Event Listener para el botón "Redo" (Rehacer).
 * Envía una petición al backend para aplicar la última acción deshecha usando la Stack de redo,
 * y luego recarga el estado para actualizar la interfaz.
 */
redoBtn.addEventListener("click", async () => {
  await fetch("/redo", { method: "POST" });
  await cargarEstado(); // Refresca el área de texto con la acción restaurada
});

/**
 * Event Listener para el botón "Limpiar".
 * Envía una petición al servidor para vaciar por completo el texto y las Stacks (historial y redo).
 * Posteriormente recarga la interfaz, dejándola en blanco.
 */
deleteBtn.addEventListener("click", async () => {
  await fetch("/limpiar", { method: "POST" });
  await cargarEstado(); // Refresca el área de texto (quedará vacía)
});

/**
 * Inicialización de la aplicación:
 * Al cargar la página por primera vez, se obtiene el estado actual almacenado en el servidor
 * para asegurar que la interfaz esté sincronizada si ya había datos previos.
 */
cargarEstado();