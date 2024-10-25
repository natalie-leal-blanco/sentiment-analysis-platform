import React, { useState } from 'react';

function SentimentDashboard() {
  const [text, setText] = useState('');
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch('http://localhost:8000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ texts: [text] }),
      });
      const data = await response.json();
      setResult(data.results[0]);
    } catch (err) {
      setError('Failed to analyze text. Please try again.');
      console.error('Error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="max-w-2xl mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6 text-center">
        Sentiment Analysis
      </h1>
      
      <div className="mb-4">
        <textarea
          className="w-full p-3 border rounded-lg shadow-sm focus:ring-2 focus:ring-blue-500"
          rows="4"
          value={text}
          onChange={(e) => setText(e.target.value)}
          placeholder="Enter text to analyze..."
          disabled={loading}
        />
      </div>

      <button
        className={`w-full bg-blue-500 text-white p-3 rounded-lg font-medium
          ${loading ? 'opacity-50 cursor-not-allowed' : 'hover:bg-blue-600'}
          transition duration-200`}
        onClick={handleAnalyze}
        disabled={loading || !text.trim()}
      >
        {loading ? 'Analyzing...' : 'Analyze Text'}
      </button>

      {error && (
        <div className="mt-4 p-3 bg-red-100 border border-red-400 text-red-700 rounded">
          {error}
        </div>
      )}

      {result && !error && (
        <div className="mt-6 p-4 bg-gray-50 rounded-lg">
          <h2 className="text-xl font-semibold mb-3">Analysis Result:</h2>
          <div className="space-y-2">
            <p className="text-lg">
              Sentiment: <span className="font-medium">{result.label}</span>
            </p>
            <p className="text-lg">
              Confidence: <span className="font-medium">
                {(result.score * 100).toFixed(2)}%
              </span>
            </p>
          </div>
        </div>
      )}
    </div>
  );
}

export default SentimentDashboard;