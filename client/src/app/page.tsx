import Image from "next/image";

export default async function Home() {
  async function getData() {
    const res = await fetch('http://127.0.0.1:8000/', {
      credentials: 'same-origin',
      mode: 'cors'
    })

    if (!res.ok) {
      // This will activate the closest `error.js` Error Boundary
      throw new Error('Failed to fetch data')
    }

    return res.json()
  }

  const data = await getData()
  console.log(data)

  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <div>
        {data.message}
      </div>
    </main>
  );
}
