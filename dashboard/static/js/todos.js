function deleteTodo(itemId) {
  fetch(`http://localhost:8000/todos/${itemId}`, {
    method: "DELETE",
  }).then(() => {
    window.location.reload();
  });
}

function updateTodo(itemId) {
  fetch(`http://localhost:8000/todos/${itemId}`)
    .then((response) => response.json())
    .then((data) => {
      const form = document.getElementById("todoForm");
      form.action = `http://localhost:8000/todos/${itemId}`;
      document.getElementById("title").value = data.title;
      document.getElementById("description").value = data.description;
      document.getElementById("status").value = data.status;
    });
}
