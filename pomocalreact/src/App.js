import "./App.css";
import { getTasks, getNotes, getSessions } from "./consumer.js";

const tasks = await getTasks();
const notes = await getNotes();
const sessions = await getSessions();

function TaskList() {
  const listItems = sessions.map(task =>
    <li
      key={task.id}
      style={{
        color: task.completed ? 'magenta' : 'darkgreen'
      }}
    >
      {task.name + ": " + task.type}
    </li>
  );

  return (
    <ul>{listItems}</ul>
  );
}

export default TaskList;