import "./App.css";

function getTasks() {
  // TODO: fetch tasks from API
  // fetch('http://127.0.0.1:8000/tasks/')
  // .then(data => {
  //   console.log(data.json())
  //   return data.json();
  // })
  return [{
    id: 1,
    name: "Add Restful API for Task",
    description: "- Necessary for downstream consumption by react",
    completed: false,
  }];
}

const tasks = getTasks();

function TaskList() {
  const listItems = tasks.map(task =>
    <li
      key={task.id}
      style={{
        color: task.completed ? 'magenta' : 'darkgreen'
      }}
    >
      {task.name + ": " + task.description}
    </li>
  );

  return (
    <ul>{listItems}</ul>
  );
}

export default TaskList;