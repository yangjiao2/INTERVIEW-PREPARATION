import React, { useState, useCallback } from 'react';
import './App.css';

const TodoList = () => {
  const [tasks, setTasks] = useState([]);
  const [newTask, setNewTask] = useState('');

  const [completedTasks, setCompletedTasks] = useState([]);
  const [incompleteTasks, setIncompleteTasks] = useState([]);

  const [selectedTasks, setSelectedTasks] = useState([]);

  const addTask = useCallback(() => {
    if (newTask.trim() !== '') {
      setIncompleteTasks((prevTasks) => [...prevTasks, { text: newTask, id: Date.now() }]);
      setNewTask('');
    }
  }, [newTask]);

  const completeTask = useCallback(
    (id) => {
      const taskToComplete = incompleteTasks.find((task) => task.id === id);
      setCompletedTasks((prevTasks) => [...prevTasks, taskToComplete]);
      deleteTask(id, 'incomplete');
    },
    [incompleteTasks]
  );

  const uncompleteTask = useCallback(
    (id) => {
      const taskToUncomplete = completedTasks.find((task) => task.id === id);
      setIncompleteTasks((prevTasks) => [...prevTasks, taskToUncomplete]);
      deleteTask(id, 'complete');
    },
    [completedTasks]
  );

  const deleteTask = useCallback(
    (id, type) => {
      if (type === 'incomplete') {
        setIncompleteTasks((prevTasks) => prevTasks.filter((task) => task.id !== id));
      } else if (type === 'complete') {
        setCompletedTasks((prevTasks) => prevTasks.filter((task) => task.id !== id));
      }
    },
    []
  );

  const toggleTaskSelection = useCallback(
    (id) => {
      setSelectedTasks((prevSelectedTasks) => {
        if (prevSelectedTasks.includes(id)) {
          return prevSelectedTasks.filter((taskId) => taskId !== id);
        } else {
          return [...prevSelectedTasks, id];
        }
      });
    },
    []
  );

  const moveSelectedTasks = useCallback(
    (targetList) => {
      const selectedTaskObjects = selectedTasks.map((taskId) => {
        return targetList.find((task) => task.id === taskId);
      });

      if (targetList === 'complete') {
        setCompletedTasks((prevTasks) => [...prevTasks, ...selectedTaskObjects]);
      } else {
        setIncompleteTasks((prevTasks) => [...prevTasks, ...selectedTaskObjects]);
      }

      setTasks((prevTasks) => prevTasks.filter((task) => !selectedTasks.includes(task.id)));
      setSelectedTasks([]);
    },
    [selectedTasks]
  );

  return (
    <div className="App">
      <h1>Todo List</h1>
      <div>
        <input
          type="text"
          value={newTask}
          onChange={(e) => setNewTask(e.target.value)}
          placeholder="Add a new task"
        />
        <button onClick={addTask}>Add</button>
      </div>
      <div>
        <h2>Incomplete</h2>
        <ul>
          {incompleteTasks.map((task) => (
            <li key={task.id}>
              <input
                type="checkbox"
                checked={selectedTasks.includes(task.id)}
                onChange={() => toggleTaskSelection(task.id)}
              />
              {task.text}
              <button onClick={() => completeTask(task.id)}>Complete</button>
              <button onClick={() => deleteTask(task.id, 'incomplete')}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
      <div>
        <h2>Done</h2>
        <ul>
          {completedTasks.map((task) => (
            <li key={task.id}>
              <input
                type="checkbox"
                checked={selectedTasks.includes(task.id)}
                onChange={() => toggleTaskSelection(task.id)}
              />
              {task.text}
              <button onClick={() => uncompleteTask(task.id)}>Undo</button>
              <button onClick={() => deleteTask(task.id, 'complete')}>Delete</button>
            </li>
          ))}
        </ul>
      </div>
      <button onClick={() => moveSelectedTasks('complete')}>Move Selected to Done</button>
      <button onClick={() => moveSelectedTasks('incomplete')}>Move Selected to Incomplete</button>
    </div>
  );
};

export default TodoList;
