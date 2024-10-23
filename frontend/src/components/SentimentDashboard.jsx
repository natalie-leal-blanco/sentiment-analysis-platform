import React, { useState } from 'react';
import InputForm from './InputForm';
import ResultsChart from './ResultsChart';
import { analyzeSentiment } from '../utils/api';
import { Alert, AlertDescription } from '@/components/ui/alert';

const SentimentDashboard = () => {
  const [data, setData] = useState([]);
  const [error, setError] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleAnalyze = async (text) => {
    setIsLoading(true);
    setError('');
    
    try {
      const result = await analyzeSentiment(text);
      setData(prevData => [...prevData, {
        timestamp: new Date().toLocaleTimeString(),
        ...result.sentiments[0]
      }].slice(-10));
    } catch (err) {
      setError('Failed to analyze sentiment. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="p-6 max-w-4xl mx-auto">
      <h1 className="text-3xl font-bold mb-6">Real-time Sentiment Analysis</h1>
      
      <InputForm onAnalyze={handleAnalyze} isLoading={isLoading} />
      
      {error && (
        <Alert variant="destructive" className="my-4">
          <AlertDescription>{error}</AlertDescription>
        </Alert>
      )}
      
      {data.length > 0 && <ResultsChart data={data} />}
    </div>
  );
};

export default SentimentDashboard;
