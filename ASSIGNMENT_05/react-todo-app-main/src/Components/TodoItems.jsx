function TodoItem({ item, index, toggleTodo, deleteTodo, startEdit }) {
  return (
    <li className="flex items-center justify-between bg-white px-4 py-2 rounded-lg shadow">
      <span
        onClick={() => toggleTodo(index)}
        className={`flex-1 cursor-pointer ${
          item.completed ? "line-through text-gray-400" : ""
        }`}
      >
        {item.text}
      </span>

      <div className="flex gap-2">
        <button
          onClick={() => startEdit(index)}
          className="text-blue-500 hover:text-blue-700"
        >
          ✏️
        </button>
        <button
          onClick={() => deleteTodo(index)}
          className="text-red-500 hover:text-red-700"
        >
          ❌
        </button>
      </div>
    </li>
  );
}

export default TodoItem;
