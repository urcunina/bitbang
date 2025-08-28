const modal = document.getElementById("modal");
// const preview = document.getElementById("preview");
let imagenSeleccionada = null;

function abrirModal() {
    modal.style.display = "flex";
}

function cerrarModal() {
    modal.style.display = "none";
    preview.innerHTML = "";
    imagenSeleccionada = null;
    document.getElementById("fileInput").value = "";
}

function previsualizarImagen(event) {
    const file = event.target.files[0];
    if (file) {
      imagenSeleccionada = file;
      const reader = new FileReader();
      reader.onload = function(e) {
        preview.innerHTML = `<img src="${e.target.result}" alt="Previsualización">`;
      }
      reader.readAsDataURL(file);
    }
  }

//   function confirmarImagen() {
//     if (imagenSeleccionada) {
//       alert("Imagen confirmada: " + imagenSeleccionada.name);
//       cerrarModal();
//     } else {
//       alert("Primero selecciona una imagen.");
//     }
//   }

//    // Cerrar modal si se hace clic fuera
//    window.onclick = function(event) {
//     if (event.target === modal) {
//       cerrarModal();
//     }
//   }

function confirmarImagen() {
    if (imagenSeleccionada) {
      const formData = new FormData();
      formData.append("imagen", imagenSeleccionada);
  
      fetch("/uploadImage", {
        method: "POST",
        body: formData,
        // headers: {
        //   "X-CSRFToken": getCookie("csrftoken") // Necesario en Django si tienes CSRF habilitado
        // }
      })
      .then(response => response.json())
      .then(data => {
        alert("Imagen subida correctamente: " + data.filename);
        cerrarModal();
        window.location.href = '/imagemanager'; // o a la página que quieras
      })
      .catch(error => {
        console.error("Error al subir la imagen:", error);
        alert("Hubo un error al subir la imagen.");
      });
    } else {
      alert("Primero selecciona una imagen.");
    }
  }

  document.querySelectorAll(".delete-btn").forEach((btn) => {
    btn.addEventListener("click", (event) => {
      const id = event.target.getAttribute("data-id");
  
      // Crear el FormData
      const formData = new FormData();
      formData.append("id", id);
  
      fetch("/deleteItem", {
        method: "POST",
        body: formData,
        // headers: {
        //   "X-CSRFToken": getCookie("csrftoken") // necesario en Django
        // }
      })
      .then(response => response.json())
      .then(data => {
        if (data.success) {
          alert("Eliminado correctamente");
          // Opcional: eliminar el elemento de la vista
          event.target.closest(".item").remove();
        } else {
          alert("Error: " + data.error);
        }
      })
      .catch(error => {
        console.error("Error en la petición:", error);
      });
    });
  });

  function logout() {
    fetch('/logout', {
        method: 'GET',
        credentials: 'include' // Incluye cookies de sesión
    })
    .then(response => {
        if (response.ok) {                                                                                                                                                                                      
            // Redirigir después de cerrar sesión
            window.location.href = '/login'; // o a la página que quieras
        } else {
            console.error('Error en logout:', response.status);
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}