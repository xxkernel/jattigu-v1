// ExerciseLevel.js
'use client';

import { useEffect, useState } from 'react';

export default function ExerciseLevel({ onSelectLevel }) {
  const [levels, setLevels] = useState([]);

  useEffect(() => {
    const fetchLevels = async () => {
      try {
        const res = await fetch(
          'http://127.0.0.1:8000/api/exercises/exercise-levels/'
        );
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await res.json();
        setLevels(data);
      } catch (error) {
        console.error('Error fetching levels:', error);
      }
    };

    fetchLevels();
  }, []);

  return (
    <select
      onChange={(e) => onSelectLevel(e.target.value)}
      className="border p-2 rounded"
    >
      <option value="all">All Levels</option>
      {levels.map((level) => (
        <option
          key={level.id}
          value={level.id}
        >
          {level.level_name}
        </option>
      ))}
    </select>
  );
}
