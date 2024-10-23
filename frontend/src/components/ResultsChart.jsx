import React from 'react';
import { LineChart, Line, XAxis, YAxis, CartesianGrid, Tooltip, Legend } from 'recharts';

const ResultsChart = ({ data }) => {
  return (
    <div className="bg-white p-4 rounded-lg shadow-lg">
      <LineChart width={800} height={400} data={data}>
        <CartesianGrid strokeDasharray="3 3" />
        <XAxis dataKey="timestamp" />
        <YAxis />
        <Tooltip />
        <Legend />
        <Line type="monotone" dataKey="positive" stroke="#4CAF50" />
        <Line type="monotone" dataKey="neutral" stroke="#2196F3" />
        <Line type="monotone" dataKey="negative" stroke="#F44336" />
      </LineChart>
    </div>
  );
};

export default ResultsChart;
