import { useLocation, Link } from 'react-router-dom';
import { ArrowLeft, Download } from 'lucide-react';
import OptimizationResults from './codeOptimizationResults';

const ResultsPage = () => {
  const location = useLocation();
  const results = location.state?.results;

  if (!results) {
    return (
      <div className="min-h-screen flex items-center justify-center">
        <div className="text-center">
          <h2 className="text-2xl font-semibold text-gray-800 mb-4">No Results Found</h2>
          <Link
            to="/"
            className="inline-flex items-center space-x-2 text-cyan-600 hover:text-cyan-700"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Back to Code Upload</span>
          </Link>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        {/* Header */}
        <div className="mb-8">
          <Link
            to="/"
            className="inline-flex items-center space-x-2 text-gray-600 hover:text-gray-800 mb-4"
          >
            <ArrowLeft className="w-4 h-4" />
            <span>Back to Upload</span>
          </Link>
          <h1 className="text-3xl font-bold text-gray-900">Optimization Results</h1>
        </div>

        {/* Stats Summary */}
        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <div className="bg-white p-6 rounded-lg shadow-sm">
            <div className="text-sm text-gray-500 mb-1">Performance Improvement</div>
            <div className="text-2xl font-bold text-cyan-600">+45%</div>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-sm">
            <div className="text-sm text-gray-500 mb-1">Code Size Reduction</div>
            <div className="text-2xl font-bold text-cyan-600">-23%</div>
          </div>
          <div className="bg-white p-6 rounded-lg shadow-sm">
            <div className="text-sm text-gray-500 mb-1">Readability Score</div>
            <div className="text-2xl font-bold text-cyan-600">9.2/10</div>
          </div>
        </div>

        {/* Results Component */}
        <OptimizationResults results={results} />

        {/* Download Section */}
        <div className="mt-8 flex justify-center">
          <button
            onClick={() => {
              // Handle download logic
              const blob = new Blob([results.optimizedCode], { type: 'text/plain' });
              const url = window.URL.createObjectURL(blob);
              const a = document.createElement('a');
              a.href = url;
              a.download = 'optimized-code.txt';
              a.click();
            }}
            className="inline-flex items-center space-x-2 px-6 py-3 bg-gray-800 text-white rounded-lg hover:bg-gray-900 transition-colors"
          >
            <Download className="w-4 h-4" />
            <span>Download Optimized Code</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default ResultsPage;