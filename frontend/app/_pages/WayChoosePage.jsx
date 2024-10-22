'use client';

import React, { useEffect, useState } from 'react';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faUserGraduate,
  faBuilding,
  faDollarSign,
  faClock,
} from '@fortawesome/free-solid-svg-icons';
import { motion } from 'framer-motion';

export default function WhyChooseUs() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      // Check if the scroll position is greater than 1000px
      if (window.scrollY > 700) {
        setIsVisible(true);
      } else {
        setIsVisible(false);
      }
    };

    window.addEventListener('scroll', handleScroll);

    // Cleanup the event listener on component unmount
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <section className="bg-white py-10 mx-10">
      <div className="container mx-auto text-center">
        <h1 className="text-4xl font-bold mb-4">Why Choose Us</h1>
        <p className="text-gray-600 mb-8">
          Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do
          eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad
          minim veniam, quis nostrud exercitation ullamco laboris nisi ut
          aliquip ex ea commodo consequat.
        </p>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-8">
          {[
            {
              icon: faUserGraduate,
              title: 'Trainer Qualifications',
              description:
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.',
            },
            {
              icon: faBuilding,
              title: 'Facility Amenities',
              description:
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.',
            },
            {
              icon: faDollarSign,
              title: 'Membership Cost',
              description:
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.',
            },
            {
              icon: faClock,
              title: 'Operating Hours',
              description:
                'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore.',
            },
          ].map(({ icon, title, description }, index) => (
            <motion.div
              key={title}
              initial={{ opacity: 0, y: 20 }} // Initial state
              animate={isVisible ? { opacity: 1, y: 0 } : { opacity: 0, y: 20 }} // Animate to this state based on isVisible
              transition={{ duration: 0.5, delay: index * 0.1 }} // Animation duration with a delay
              className="flex flex-col items-center bg-gray-100 p-4 rounded-lg shadow-md"
            >
              <div className="mb-2 text-5xl text-gray-700">
                <FontAwesomeIcon icon={icon} />
              </div>
              <h2 className="text-xl font-semibold mb-2">{title}</h2>
              <p className="text-gray-500">{description}</p>
            </motion.div>
          ))}
        </div>
      </div>
    </section>
  );
}
