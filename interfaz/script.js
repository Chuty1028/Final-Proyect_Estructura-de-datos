// Referencias correctas a los elementos del HTML
const editor = document.getElementById("noteArea");   // textarea (id="noteArea" en el HTML)
const undoBtn = document.getElementById("undoBtn");
const redoBtn = document.getElementById("redoBtn");
const deleteBtn = document.getElementById("deleteBtn"); // botón "Limpiar"

// Carga el estado actual desde el servidor y actualiza el textarea
async function cargarEstado() {
  const respuesta = await fetch("/estado");
  const data = await respuesta.json();
  editor.value = data.texto;
}
//async le dice a js que esa funcion va a esperar cosas
// Cada vez que el usuario escribe una letra en el textarea, sincroniza con el backend
// Una letra es una accion por eso se borra letra por letra a la hora de hacer undo
editor.addEventListener("input", async () => {
  await fetch("/actualizar", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ texto: editor.value })
  });
});

//await espera hasta que el servidor responda y carga el estado actualizado y lo muestra en pantalla
// Botón Undo: deshace la última acción y recarga el texto
undoBtn.addEventListener("click", async () => {
  await fetch("/undo", { method: "POST" });
  await cargarEstado();
});

// Botón Redo: rehace la última acción deshecha y recarga el texto
redoBtn.addEventListener("click", async () => {
  await fetch("/redo", { method: "POST" });
  await cargarEstado();
});

// Botón Limpiar: borra todo el texto e historial, luego recarga
deleteBtn.addEventListener("click", async () => {
  await fetch("/limpiar", { method: "POST" });
  await cargarEstado();
});

// Al cargar la página, obtiene el estado actual del servidor
cargarEstado();