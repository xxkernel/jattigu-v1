'use client';

import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import {
  faFacebook,
  faTwitter,
  faInstagram,
  faLinkedin,
} from '@fortawesome/free-brands-svg-icons';

export default function FooterPage() {
  return (
    <footer className="bg-gray-900 text-white py-10">
      <div className="container mx-auto px-6 lg:px-8">
        <div className="grid grid-cols-1 md:grid-cols-3 gap-10">
          <div>
            <h3 className="text-lg font-semibold mb-4">Quick Links</h3>
            <ul className="space-y-2">
              <li>
                <a
                  href="#"
                  className="hover:underline"
                >
                  Home
                </a>
              </li>
              <li>
                <a
                  href="#"
                  className="hover:underline"
                >
                  About Us
                </a>
              </li>
              <li>
                <a
                  href="#"
                  className="hover:underline"
                >
                  Services
                </a>
              </li>
              <li>
                <a
                  href="#"
                  className="hover:underline"
                >
                  Blog
                </a>
              </li>
              <li>
                <a
                  href="#"
                  className="hover:underline"
                >
                  Contact
                </a>
              </li>
            </ul>
          </div>
          <div>
            <h3 className="text-lg font-semibold mb-4">Contact Us</h3>
            <p className="mb-2">123 Fitness St, Suite 456</p>
            <p className="mb-2">City, State, ZIP</p>
            <p className="mb-2">Email: info@example.com</p>
            <p className="mb-2">Phone: (123) 456-7890</p>
          </div>
          <div>
            <h3 className="text-lg font-semibold mb-4">Follow Us</h3>
            <div className="flex space-x-4">
              <a
                href="#"
                className="text-gray-400 hover:text-white"
              >
                <FontAwesomeIcon
                  icon={faFacebook}
                  className="h-6 w-6"
                />
              </a>
              <a
                href="#"
                className="text-gray-400 hover:text-white"
              >
                <FontAwesomeIcon
                  icon={faTwitter}
                  className="h-6 w-6"
                />
              </a>
              <a
                href="#"
                className="text-gray-400 hover:text-white"
              >
                <FontAwesomeIcon
                  icon={faInstagram}
                  className="h-6 w-6"
                />
              </a>
              <a
                href="#"
                className="text-gray-400 hover:text-white"
              >
                <FontAwesomeIcon
                  icon={faLinkedin}
                  className="h-6 w-6"
                />
              </a>
            </div>
          </div>
        </div>
        <div className="mt-10 border-t border-gray-700 pt-4 text-center">
          <p className="text-sm text-gray-400">
            &copy; {new Date().getFullYear()} Your Company Name. All rights
            reserved.
          </p>
        </div>
      </div>
    </footer>
  );
}
