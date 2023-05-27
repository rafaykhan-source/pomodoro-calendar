
async function getTasks() {
    const response = await fetch("http://127.0.0.1:8000/tasks/");
    const jsonData = await response.json();
    return jsonData;
  }

async function getNotes() {
    const response = await fetch("http://127.0.0.1:8000/notes/");
    const jsonData = await response.json();
    return jsonData;
}

async function getSessions() {
    const response = await fetch("http://127.0.0.1:8000/sessions/");
    const jsonData = await response.json();
    return jsonData;
}
export { getTasks, getNotes, getSessions };