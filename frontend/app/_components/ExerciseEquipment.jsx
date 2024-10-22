// ExerciseEquipment.js
'use client';

import { useEffect, useState } from 'react';

export default function ExerciseEquipment({ onSelectEquipment }) {
  const [equipments, setEquipments] = useState([]);

  useEffect(() => {
    const fetchEquipments = async () => {
      try {
        const res = await fetch(
          'http://127.0.0.1:8000/api/exercises/equipment/'
        );
        if (!res.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await res.json();
        setEquipments(data);
      } catch (error) {
        console.error('Error fetching equipments:', error);
      }
    };

    fetchEquipments();
  }, []);

  return (
    <select
      onChange={(e) => onSelectEquipment(e.target.value)}
      className="border p-2 rounded"
    >
      <option value="all">All Equipment</option>
      {equipments.map((equipment) => (
        <option
          key={equipment.id}
          value={equipment.id}
        >
          {equipment.equipment_name}
        </option>
      ))}
    </select>
  );
}
