import { useState } from 'react';
import { Button } from './ui/button';
import { Input } from './ui/input';
import { Checkbox } from './ui/checkbox';

interface Todo {
  id: number;
  text: string;
  completed: boolean;
}

export default function TodoList() {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [input, setInput] = useState('');

  const addTodo = () => {
    if (input.trim() === '') return;
    setTodos([...todos, { id: Date.now(), text: input, completed: false }]);
    setInput('');
  };

  const toggleTodo = (id: number) => {
    setTodos(todos => todos.map(todo => todo.id === id ? { ...todo, completed: !todo.completed } : todo));
  };

  const removeTodo = (id: number) => {
    setTodos(todos => todos.filter(todo => todo.id !== id));
  };

  return (
    <div className="w-full max-w-md">
      <div className="flex gap-2 mb-4">
        <Input
          placeholder="Adicionar tarefa..."
          value={input}
          onChange={e => setInput(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && addTodo()}
        />
        <Button onClick={addTodo}>Adicionar</Button>
      </div>
      <ul className="space-y-2">
        {todos.map(todo => (
          <li key={todo.id} className="flex items-center gap-2 bg-white p-2 rounded shadow">
            <Checkbox checked={todo.completed} onCheckedChange={() => toggleTodo(todo.id)} />
            <span className={todo.completed ? 'line-through text-gray-400 flex-1' : 'flex-1'}>{todo.text}</span>
            <Button variant="destructive" size="sm" onClick={() => removeTodo(todo.id)}>
              Remover
            </Button>
          </li>
        ))}
      </ul>
    </div>
  );
}
