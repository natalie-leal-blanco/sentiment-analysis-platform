import React, { useState } from 'react';
import { Alert, AlertDescription } from '@/components/ui/alert';

const InputForm = ({ onAnalyze, isLoading }) => {
  const [input, setInput] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    onAnalyze(input);
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <textarea
        className="w-full p-2 border rounded-md"
        rows={4}
        value={input}
        onChange={(e) => setInput(e.target.value)}
        placeholder="Enter text to analyze..."
      />
      <button
        type="submit"
        disabled={isLoading}
        className={`px-4 py-2 bg-blue-600 text-white rounded-md 
          ${isLoading ? 'opacity-50 cursor-not-allowed' : 'hover:bg-blue-700'}`}
      >
        {isLoading ? 'Analyzing...' : 'Analyze Sentiment'}
      </button>
    </form>
  );
};

export default InputForm;
