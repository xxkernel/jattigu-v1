// components/AddExercise.js
import { useState } from 'react';

const AddExercise = () => {
  const [formData, setFormData] = useState({
    name: '',
    description: '',
    duration: '',
    intensity: 'Low',
    category: [],
    level: '',
    equipment: [],
    calories: '',
    image: null,
    video_url: '',
  });

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({ ...formData, [name]: value });
  };

  const handleFileChange = (e) => {
    setFormData({ ...formData, image: e.target.files[0] });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    const data = new FormData();
    for (const key in formData) {
      data.append(key, formData[key]);
    }

    try {
      const response = await fetch(
        'http://127.0.0.1:8000/api/exercises/add_exercise/',
        {
          method: 'POST',
          body: data,
        }
      );

      if (response.ok) {
        const result = await response.json();
        console.log('Exercise added:', result);
        setFormData({
          name: '',
          description: '',
          duration: '',
          intensity: 'Low',
          category: [],
          level: '',
          equipment: [],
          calories: '',
          image: null,
          video_url: '',
        });
      } else {
        console.error('Error adding exercise:', response.statusText);
      }
    } catch (error) {
      console.error('Fetch error:', error);
    }
  };

  return (
    <div className="max-w-md mx-auto p-4 border rounded-lg shadow-lg bg-white">
      <h2 className="text-2xl font-bold mb-4 text-center">Add New Exercise</h2>
      <form
        onSubmit={handleSubmit}
        className="space-y-4"
      >
        <input
          type="text"
          name="name"
          placeholder="Exercise Name"
          value={formData.name}
          onChange={handleChange}
          required
          className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <textarea
          name="description"
          placeholder="Description"
          value={formData.description}
          onChange={handleChange}
          required
          className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="number"
          name="duration"
          placeholder="Duration in minutes"
          value={formData.duration}
          onChange={handleChange}
          required
          className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <select
          name="intensity"
          onChange={handleChange}
          className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        >
          <option value="Low">Low</option>
          <option value="Medium">Medium</option>
          <option value="High">High</option>
        </select>
        <input
          type="number"
          name="calories"
          placeholder="Calories burned per minute"
          value={formData.calories}
          onChange={handleChange}
          required
          className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="file"
          name="image"
          onChange={handleFileChange}
          className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <input
          type="text"
          name="video_url"
          placeholder="Video URL"
          value={formData.video_url}
          onChange={handleChange}
          className="w-full p-2 border rounded focus:outline-none focus:ring-2 focus:ring-blue-500"
        />
        <button
          type="submit"
          className="w-full bg-blue-500 text-white py-2 rounded hover:bg-blue-600 transition duration-200"
        >
          Add Exercise
        </button>
      </form>
    </div>
  );
};

export default AddExercise;
