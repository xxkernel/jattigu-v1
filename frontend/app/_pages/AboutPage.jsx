'use client';

import {
  CloudArrowUpIcon,
  LockClosedIcon,
  ServerIcon,
} from '@heroicons/react/20/solid';
import { motion } from 'framer-motion';
import { useEffect, useState } from 'react';

const features = [
  {
    name: 'Push to deploy.',
    description:
      'Lorem ipsum, dolor sit amet consectetur adipisicing elit. Maiores impedit perferendis suscipit eaque, iste dolor cupiditate blanditiis ratione.',
    icon: CloudArrowUpIcon,
  },
  {
    name: 'SSL certificates.',
    description:
      'Anim aute id magna aliqua ad ad non deserunt sunt. Qui irure qui lorem cupidatat commodo.',
    icon: LockClosedIcon,
  },
  {
    name: 'Database backups.',
    description:
      'Ac tincidunt sapien vehicula erat auctor pellentesque rhoncus. Et magna sit morbi lobortis.',
    icon: ServerIcon,
  },
];

const fadeIn = {
  hidden: { opacity: 0, y: 20 },
  visible: { opacity: 1, y: 0 },
};

export default function AboutPage() {
  const [isVisible, setIsVisible] = useState(false);

  useEffect(() => {
    const handleScroll = () => {
      if (window.scrollY >= 300) {
        setIsVisible(true);
      } else {
        setIsVisible(false);
      }
    };

    window.addEventListener('scroll', handleScroll);
    return () => {
      window.removeEventListener('scroll', handleScroll);
    };
  }, []);

  return (
    <div className="overflow-hidden bg-white py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto grid max-w-2xl grid-cols-1 gap-x-8 gap-y-16 sm:gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-2">
          <div className="lg:pr-8 lg:pt-4">
            <div className="lg:max-w-lg">
              <motion.h2
                initial="hidden"
                animate={isVisible ? 'visible' : 'hidden'}
                variants={fadeIn}
                transition={{ duration: 0.6 }}
                className="text-base font-semibold leading-7 text-indigo-600"
              >
                Deploy faster
              </motion.h2>
              <motion.p
                initial="hidden"
                animate={isVisible ? 'visible' : 'hidden'}
                variants={fadeIn}
                transition={{ duration: 0.6, delay: 0.1 }}
                className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl"
              >
                A better workflow
              </motion.p>
              <motion.p
                initial="hidden"
                animate={isVisible ? 'visible' : 'hidden'}
                variants={fadeIn}
                transition={{ duration: 0.6, delay: 0.2 }}
                className="mt-6 text-lg leading-8 text-gray-600"
              >
                Lorem ipsum, dolor sit amet consectetur adipisicing elit.
                Maiores impedit perferendis suscipit eaque, iste dolor
                cupiditate blanditiis ratione.
              </motion.p>
              <dl className="mt-10 max-w-xl space-y-8 text-base leading-7 text-gray-600 lg:max-w-none">
                {features.map((feature, index) => (
                  <motion.div
                    key={feature.name}
                    className="relative pl-9"
                    initial="hidden"
                    animate={isVisible ? 'visible' : 'hidden'}
                    variants={fadeIn}
                    transition={{ duration: 0.6, delay: 0.3 + index * 0.1 }} // Stagger animation for features
                  >
                    <dt className="inline font-semibold text-gray-900">
                      <feature.icon
                        aria-hidden="true"
                        className="absolute left-1 top-1 h-5 w-5 text-indigo-600"
                      />
                      {feature.name}
                    </dt>{' '}
                    <dd className="inline">{feature.description}</dd>
                  </motion.div>
                ))}
              </dl>
            </div>
          </div>
          <motion.img
            initial="hidden"
            animate={isVisible ? 'visible' : 'hidden'}
            variants={fadeIn}
            transition={{ duration: 0.6, delay: 0.4 }}
            alt="Product screenshot"
            src="https://images.unsplash.com/photo-1521805103424-d8f8430e8933?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
            width={2432}
            height={1442}
            className="w-[48rem] h-[520px] max-w-none rounded-xl shadow-xl ring-1 ring-gray-400/10 sm:w-[57rem] md:-ml-4 lg:-ml-0"
          />
        </div>
      </div>
    </div>
  );
}
