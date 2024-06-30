const baseUrl = 'http://0.0.0.0:8000'; // Replace with your API endpoint
const startId = 1234567;
const totalRequests = 100000; // 1 lakh

interface UniqueJson {
  name: string;
  email: string;
  address: string;
  phone: number;
  company: string;
  randomData: string;
}

interface Payload {
  id: number;
  data: UniqueJson;
}

function generateUniqueJson(): UniqueJson {
  return {
    name: Math.random().toString(36).substring(7),
    email: Math.random().toString(36).substring(7) + '@example.com',
    address: Math.random().toString(36).substring(7) + ' Street',
    phone: Math.floor(Math.random() * 10000000000),
    company: Math.random().toString(36).substring(7) + ' Inc.',
    randomData: Math.random().toString(36).substring(7) + ' ' + Math.random().toString(36).substring(7)
  };
}

async function sendRequest(id: number): Promise<void> {
  const payload: Payload = {
    id: id,
    data: generateUniqueJson()
  };

  try {
    const response = await fetch(`${baseUrl}/create/${id}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload)
    });

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }

    console.log(`Request ${id - startId + 1} sent successfully`);
  } catch (error) {
    console.error(`Error sending request ${id - startId + 1}:`, (error as Error).message);
  }
}

async function sendBatchRequests(): Promise<void> {
  for (let i = 0; i < totalRequests; i++) {
    const currentId = startId + i;
    await sendRequest(currentId);
  }
}

sendBatchRequests()
  .then(() => console.log('All requests sent'))
  .catch(error => console.error('Error in batch process:', error));