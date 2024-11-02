import React from 'react';
import { useState, useEffect } from 'react';
import { Check, Code, FileText, Copy, ExternalLink } from 'lucide-react';

const OptimizationResults = ({ isLoading, results }) => {
  const [copied, setCopied] = useState(false);
  const [activeTab, setActiveTab] = useState('code');

  const copyToClipboard = async (text) => {
    await navigator.clipboard.writeText(text);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };

  if (isLoading) {
    return (
      <div className="flex flex-col items-center justify-center min-h-[400px] w-full">
        <div className="relative">
          {/* Animated code blocks loader */}
          <div className="w-16 h-16 relative">
            <div className="absolute inset-0 animate-pulse">
              <div className="h-3 w-12 bg-cyan-600/20 rounded mb-2"></div>
              <div className="h-3 w-16 bg-cyan-600/30 rounded mb-2"></div>
              <div className="h-3 w-10 bg-cyan-600/40 rounded"></div>
            </div>
            <div className="absolute inset-0 animate-pulse delay-150">
              <div className="h-3 w-14 bg-blue-600/20 rounded mb-2"></div>
              <div className="h-3 w-11 bg-blue-600/30 rounded mb-2"></div>
              <div className="h-3 w-16 bg-blue-600/40 rounded"></div>
            </div>
          </div>
        </div>
        <p className="text-gray-600 mt-6 animate-pulse">Optimizing your code with AI...</p>
        <div className="text-sm text-gray-500 mt-2">This may take a few moments</div>
      </div>
    );
  }

  if (!results) return null;

  return (
    <div className="w-full max-w-4xl mx-auto bg-white rounded-xl shadow-lg overflow-hidden">
      {/* Header */}
      <div className="bg-gradient-to-r from-cyan-600 to-blue-600 p-6 text-white">
        <div className="flex items-center space-x-2">
          <Check className="w-6 h-6" />
          <h2 className="text-xl font-semibold">Optimization Complete</h2>
        </div>
      </div>

      {/* Tabs */}
      <div className="border-b border-gray-200">
        <div className="flex space-x-1 p-4">
          <button
            onClick={() => setActiveTab('code')}
            className={`px-4 py-2 rounded-lg flex items-center space-x-2 transition-colors ${
              activeTab === 'code'
                ? 'bg-cyan-100 text-cyan-700'
                : 'text-gray-600 hover:bg-gray-100'
            }`}
          >
            <Code className="w-4 h-4" />
            <span>Optimized Code</span>
          </button>
          <button
            onClick={() => setActiveTab('explanation')}
            className={`px-4 py-2 rounded-lg flex items-center space-x-2 transition-colors ${
              activeTab === 'explanation'
                ? 'bg-cyan-100 text-cyan-700'
                : 'text-gray-600 hover:bg-gray-100'
            }`}
          >
            <FileText className="w-4 h-4" />
            <span>Explanations</span>
          </button>
        </div>
      </div>

      {/* Content */}
      <div className="p-6">
        {activeTab === 'code' ? (
          <div className="relative text-left">
            <pre className="bg-gray-50 rounded-lg p-4 overflow-x-auto text-sm font-mono">
              {results.optimizedCode}
            </pre>
            <button
              onClick={() => copyToClipboard(results.optimizedCode)}
              className="absolute top-4 right-4 p-2 rounded-lg bg-white/80 hover:bg-white shadow-sm hover:shadow transition-all"
              title="Copy code"
            >
              {copied ? (
                <Check className="w-4 h-4 text-green-500" />
              ) : (
                <Copy className="w-4 h-4 text-gray-500" />
              )}
            </button>
          </div>
        ) : (
          <div className="space-y-4 text-left">
            {results.explanation.split('\n').map((paragraph, index) => (
              <p key={index} className="text-gray-700 leading-relaxed">
                {paragraph}
              </p>
            ))}
          </div>
        )}
      </div>

      {/* Footer */}
      <div className="bg-gray-50 p-4 border-t border-gray-200">
        <div className="flex items-center justify-between">
          <span className="text-sm text-gray-600">
            Optimized using advanced AI algorithms
          </span>
          <button
            onClick={() => copyToClipboard(results.optimizedCode)}
            className="flex items-center space-x-2 text-sm text-cyan-600 hover:text-cyan-700 transition-colors"
          >
            <ExternalLink className="w-4 h-4" />
            <span>Export Code</span>
          </button>
        </div>
      </div>
    </div>
  );
};

export default OptimizationResults;