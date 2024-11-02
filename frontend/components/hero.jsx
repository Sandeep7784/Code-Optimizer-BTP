import { useState } from "react";
import CodeUploadForm from "./codeUploadForm";
import Modal from "./modal";

const Hero = () => {
  const [showForm, setShowForm] = useState(false);

  const toggleForm = () => {
    setShowForm(!showForm);
  };

  return (
    <div className="container mx-auto px-6 mt-24 md:mt-30">
      <div className="flex items-center justify-center">
        <div className="w-full max-w-6xl">
          {" "}
          {/* Increased from max-w-4xl */}
          <div className="flex flex-col items-center text-center space-y-8">
            {" "}
            {/* Increased space-y-6 to space-y-8 */}
            {/* Main Heading with gradient effect */}
            <p className="text-2xl md:text-3xl font-medium text-gray-700 tracking-wide">
              Welcome to Code Optimizer 🚀
            </p>
            <h1 className="text-4xl md:text-5xl lg:text-7xl font-extrabold tracking-tight max-w-5xl">
              {" "}
              {/* Increased text size and max-width */}
              Transform Your Code with{" "}
              <span className="bg-gradient-to-r from-cyan-600 to-blue-600 bg-clip-text text-transparent">
                intelligent optimization.
              </span>
            </h1>
            {/* Subheading text */}
            <p className="text-gray-600 max-w-3xl mx-auto text-lg md:text-xl leading-relaxed">
              {" "}
              {/* Increased max-width and text size */}
              Elevate your code quality instantly with our advanced optimization
              engine. Get cleaner, faster, and more maintainable code with just
              a few clicks. Perfect for developers who value both performance
              and readability.
            </p>
            {/* Buttons container with more spacing */}
            <div className="flex flex-col sm:flex-row gap-6 mt-10">
              {" "}
              {/* Increased gap and margin */}
              <button
                onClick={toggleForm}
                className="group px-10 py-4 bg-gradient-to-r from-cyan-600 to-blue-600 text-white rounded-lg font-medium hover:from-cyan-700 hover:to-blue-700 transition-all duration-200 shadow-lg hover:shadow-xl flex items-center justify-center space-x-2 text-lg" /* Increased padding and text size */
              >
                <span>Optimize Now</span>
                <svg
                  className="w-6 h-6 group-hover:translate-x-1 transition-transform duration-200"
                  fill="none"
                  stroke="currentColor"
                  viewBox="0 0 24 24"
                >
                  <path
                    strokeLinecap="round"
                    strokeLinejoin="round"
                    strokeWidth={2}
                    d="M13 7l5 5m0 0l-5 5m5-5H6"
                  />
                </svg>
              </button>
            </div>
            {/* Feature highlights with more spacing */}
            <div className="grid grid-cols-1 md:grid-cols-3 gap-10 mt-20 w-full">
              {" "}
              {/* Increased gap and margin */}
              <div className="p-6 bg-white rounded-xl hover:shadow-lg transition-shadow duration-200">
                <div className="text-cyan-600 mb-4">
                  <svg
                    className="w-10 h-10 mx-auto"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M13 10V3L4 14h7v7l9-11h-7z"
                    />
                  </svg>
                </div>
                <h3 className="font-semibold text-xl mb-2">Lightning Fast</h3>
                <p className="text-gray-600">Optimize your code in seconds</p>
              </div>
              <div className="p-6 bg-white rounded-xl hover:shadow-lg transition-shadow duration-200">
                <div className="text-cyan-600 mb-4">
                  <svg
                    className="w-10 h-10 mx-auto"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M9 12l2 2 4-4m5.618-4.016A11.955 11.955 0 0112 2.944a11.955 11.955 0 01-8.618 3.04A12.02 12.02 0 003 9c0 5.591 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.042-.133-2.052-.382-3.016z"
                    />
                  </svg>
                </div>
                <h3 className="font-semibold text-xl mb-2">Secure & Private</h3>
                <p className="text-gray-600">Your code stays confidential</p>
              </div>
              <div className="p-6 bg-white rounded-xl hover:shadow-lg transition-shadow duration-200">
                <div className="text-cyan-600 mb-4">
                  <svg
                    className="w-10 h-10 mx-auto"
                    fill="none"
                    stroke="currentColor"
                    viewBox="0 0 24 24"
                  >
                    <path
                      strokeLinecap="round"
                      strokeLinejoin="round"
                      strokeWidth={2}
                      d="M4 4v5h.582m15.356 2A8.001 8.001 0 004.582 9m0 0H9m11 11v-5h-.581m0 0a8.003 8.003 0 01-15.357-2m15.357 2H15"
                    />
                  </svg>
                </div>
                <h3 className="font-semibold text-xl mb-2">
                  Smart Suggestions
                </h3>
                <p className="text-gray-600">AI-powered improvements</p>
              </div>
            </div>
          </div>
          {/* Modal */}
          {showForm && (
            <Modal onClose={toggleForm}>
              <CodeUploadForm />
            </Modal>
          )}
        </div>
      </div>
    </div>
  );
};

export default Hero;
