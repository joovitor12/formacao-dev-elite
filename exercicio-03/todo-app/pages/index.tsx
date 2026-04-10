import Head from 'next/head';
import TodoList from '../components/TodoList';

export default function Home() {
  return (
    <>
      <Head>
        <title>Todo App</title>
      </Head>
      <main className="min-h-screen bg-gray-50 flex flex-col items-center justify-center p-4">
        <h1 className="text-3xl font-bold mb-6">Todo App</h1>
        <TodoList />
      </main>
    </>
  );
}
