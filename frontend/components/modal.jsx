import React from "react";

const Modal = ({ children, onClose }) => {
  return (
    <div className="fixed inset-0 z-50 flex items-center justify-center bg-gray-900/50 backdrop-blur-sm">
      <div className="relative w-full max-w-lg mx-4 sm:mx-0">
        {/* Modal Content */}
        <div className="relative bg-white rounded-xl shadow-2xl p-8 border border-gray-100">
          {/* Close Button */}
          <button
            onClick={onClose}
            className="absolute top-4 right-4 p-2 rounded-lg text-gray-400 hover:text-gray-600 hover:bg-gray-100 transition-all duration-200 focus:outline-none focus:ring-2 focus:ring-cyan-500 focus:ring-opacity-50"
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              className="h-5 w-5"
              fill="none"
              viewBox="0 0 24 24"
              stroke="currentColor"
              strokeWidth={2}
            >
              <path
                strokeLinecap="round"
                strokeLinejoin="round"
                d="M6 18L18 6M6 6l12 12"
              />
            </svg>
          </button>

          {/* Header Line */}
          <div className="h-1 w-16 bg-gradient-to-r from-cyan-600 to-blue-600 rounded-full mb-6" />

          {/* Modal Content */}
          <div className="space-y-6">
            {children}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Modal;