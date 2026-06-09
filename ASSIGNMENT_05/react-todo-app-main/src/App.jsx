import { useState, useEffect } from "react";

function App() {

  // 🔹 State (ALWAYS first)
  const [todo, setTodo] = useState("");
  const [todos, setTodos] = useState([]);

  // 🔹 Load todos from localStorage on first render
  useEffect(() => {
    const savedTodos = localStorage.getItem("todos");
    if (savedTodos) {
      setTodos(JSON.parse(savedTodos));
    }
  }, []);

  // 🔹 Save todos to localStorage whenever todos change
  useEffect(() => {
    localStorage.setItem("todos", JSON.stringify(todos));
  }, [todos]);

  // 🔹 Add todo
  function addTodo() {
    if (todo.trim() === "") return;

    setTodos([...todos, { text: todo, completed: false }]);
    setTodo("");
  }

  // 🔹 Delete todo
  function deleteTodo(index) {
    setTodos(todos.filter((_, i) => i !== index));
  }

  // 🔹 Toggle completed
  function toggleTodo(index) {
    const updated = [...todos];
    updated[index].completed = !updated[index].completed;
    setTodos(updated);
  }

  return (
    <div style={styles.container}>
      <h1 style={styles.heading}>📝 Todo App</h1>

      <div style={styles.inputBox}>
        <input
          value={todo}
          onChange={(e) => setTodo(e.target.value)}
          onKeyDown={(e) => {
            if (e.key === "Enter") {
              addTodo();
            }
          }}
          placeholder="Enter a task..."
          style={styles.input}
        />

        <button onClick={addTodo} style={styles.button}>
          Add
        </button>
      </div>

      <ul style={styles.list}>
        {todos.map((item, index) => (
          <li key={index} style={styles.item}>
            <span
              onClick={() => toggleTodo(index)}
              style={{
                textDecoration: item.completed ? "line-through" : "none",
                cursor: "pointer",
                flex: 1,
              }}
            >
              {item.text}
            </span>

            <button
              onClick={() => deleteTodo(index)}
              style={styles.delete}
            >
              ❌
            </button>
          </li>
        ))}
      </ul>

      {todos.length === 0 && (
        <p style={styles.empty}>No tasks yet 🌱</p>
      )}
    </div>
  );
}

// 🎨 Styles
const styles = {
  container: {
    minHeight: "100vh",
    background: "#f5f7fb",
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
    paddingTop: "50px",
    fontFamily: "Arial, sans-serif",
    maxWidth: "400px",
    margin: "auto",
  },
  heading: {
    marginBottom: "20px",
  },
  inputBox: {
    display: "flex",
    gap: "10px",
    marginBottom: "20px",
  },
  input: {
    padding: "10px",
    fontSize: "16px",
    width: "220px",
    borderRadius: "6px",
    border: "1px solid #ccc",
  },
  button: {
    padding: "10px 16px",
    fontSize: "16px",
    cursor: "pointer",
    background: "#4f46e5",
    color: "#fff",
    border: "none",
    borderRadius: "6px",
  },
  list: {
    listStyle: "none",
    padding: 0,
    width: "100%",
  },
  item: {
    background: "#fff",
    padding: "10px",
    marginBottom: "8px",
    borderRadius: "6px",
    display: "flex",
    alignItems: "center",
    gap: "10px",
    boxShadow: "0 2px 5px rgba(0,0,0,0.1)",
  },
  delete: {
    background: "transparent",
    border: "none",
    cursor: "pointer",
    fontSize: "16px",
  },
  empty: {
    marginTop: "20px",
    color: "#666",
  },
};

export default App;

