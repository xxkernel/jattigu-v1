// Page.js
'use client';

import { useState } from 'react';
import Header from '../_components/Header';
import ExerciseCategory from '../_components/ExerciseCategory';
import ExerciseLevel from '../_components/ExerciseLevel';
import ExerciseEquipment from '../_components/ExerciseEquipment';
import Exercises from '../_components/Exercises';
import AddExercise from '../_components/AddExercise';

export default function Page() {
  const [selectedCategory, setSelectedCategory] = useState('all');
  const [selectedLevel, setSelectedLevel] = useState('all');
  const [selectedEquipment, setSelectedEquipment] = useState('all');

  return (
    <div>
      <Header />
      <div className="flex space-x-4 mb-4 justify-center">
        <ExerciseCategory onSelectCategory={setSelectedCategory} />
        <ExerciseLevel onSelectLevel={setSelectedLevel} />
        <ExerciseEquipment onSelectEquipment={setSelectedEquipment} />
      </div>
      {/* <AddExercise /> */}
      <Exercises
        selectedCategory={selectedCategory}
        selectedLevel={selectedLevel}
        selectedEquipment={selectedEquipment}
      />
    </div>
  );
}
