const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

export const analyzeSentiment = async (text) => {
  try {
    const response = await fetch(`${API_URL}/analyze`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ texts: [text] }),
    });

    if (!response.ok) {
      throw new Error('Analysis failed');
    }

    return await response.json();
  } catch (error) {
    console.error('API Error:', error);
    throw error;
  }
};
