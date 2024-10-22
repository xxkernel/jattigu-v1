// Exercises.js
'use client';

import Link from 'next/link';
import { useEffect, useState } from 'react';

export default function Exercises({
  selectedCategory,
  selectedLevel,
  selectedEquipment,
}) {
  const [exercises, setExercises] = useState([]);

  useEffect(() => {
    const fetchExercises = async () => {
      try {
        const res = await fetch('http://127.0.0.1:8000/api/exercises/');
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await res.json();
        setExercises(data);
      } catch (error) {
        console.error('Error fetching exercises:', error);
      }
    };

    fetchExercises();
  }, []);

  const filteredExercises = exercises.filter((exercise) => {
    let matchesCategory = true;
    let matchesLevel = true;
    let matchesEquipment = true;

    if (selectedCategory) {
      if (selectedCategory === 'all') {
        matchesCategory = true;
      } else {
        matchesCategory = exercise.category.includes(+selectedCategory);
      }
    }
    if (selectedLevel) {
      if (selectedLevel === 'all') {
        matchesLevel = true;
      } else {
        matchesLevel = exercise.level == selectedLevel;
      }
    }
    if (selectedEquipment) {
      if (selectedEquipment === 'all') {
        matchesEquipment = true;
      } else {
        matchesEquipment = exercise.equipment.includes(+selectedEquipment);
      }
    }

    return matchesCategory && matchesLevel && matchesEquipment;
  });

  return (
    <div className="bg-white">
      <div className="mx-auto max-w-2xl px-4 py-16 sm:px-6 sm:py-24 lg:max-w-7xl lg:px-8">
        <h2 className="text-2xl font-bold tracking-tight text-gray-900">
          Exercises
        </h2>

        <div className="mt-6 grid grid-cols-1 gap-x-6 gap-y-10 sm:grid-cols-2 lg:grid-cols-4 xl:gap-x-8">
          {filteredExercises.map((exercise) => (
            <div
              key={exercise.id}
              className="group relative"
            >
              <div className="aspect-h-1 aspect-w-1 w-full overflow-hidden rounded-md bg-gray-200 lg:aspect-none group-hover:opacity-75 lg:h-80">
                <img
                  src={exercise.image}
                  alt={exercise.name}
                  className="h-full w-full object-cover object-center lg:h-full lg:w-full"
                />
              </div>
              <div className="mt-4 flex justify-between">
                <div>
                  <h3 className="text-sm text-gray-700">
                    <Link href={`/exercises/${exercise.id}`}>
                      <span
                        aria-hidden="true"
                        className="absolute inset-0"
                      />
                      {exercise.name}
                    </Link>
                  </h3>
                  <p className="mt-1 text-sm text-gray-500">
                    {exercise.intensity}
                  </p>
                </div>
                <p className="text-sm font-medium text-gray-900">
                  {exercise.calories} calories
                </p>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
}
