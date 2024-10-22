// ExerciseCategory.js
'use client';

import { useEffect, useState } from 'react';

export default function ExerciseCategory({ onSelectCategory }) {
  const [categories, setCategories] = useState([]);

  useEffect(() => {
    const fetchCategories = async () => {
      try {
        const res = await fetch(
          'http://127.0.0.1:8000/api/exercises/exercise-categories/'
        );
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await res.json();
        setCategories(data);
      } catch (error) {
        console.error('Error fetching categories:', error);
      }
    };

    fetchCategories();
  }, []);

  return (
    <select
      onChange={(e) => onSelectCategory(e.target.value)}
      className="border p-2 rounded"
    >
      <option value="all">All Categories</option>
      {categories.map((category) => (
        <option
          key={category.id}
          value={category.id}
        >
          {category.category_name}
        </option>
      ))}
    </select>
  );
}
