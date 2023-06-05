function deleteCourse(itemId) {
  console.log(itemId);
  fetch(`http://localhost:8000/courses/${itemId}`, {
    method: "DELETE",
  }).then(() => {
    window.location.reload();
  });
}

function updateCourse(itemId) {
  fetch(`http://localhost:8000/courses/${itemId}`)
    .then((response) => response.json())
    .then((data) => {
      const form = document.getElementById("courseForm");
      form.action = `http://localhost:8000/courses/${itemId}`;
      document.getElementById("name").value = data.name;
      document.getElementById("room").value = data.room;
      document.getElementById("day").value = data.day;
    });
}
