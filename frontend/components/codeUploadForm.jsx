import React, { useState, useRef } from 'react';
import { Upload, X, Eye } from 'lucide-react';
import OptimizationResults from './codeOptimizationResults';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';

const CodeUploadForm = () => {
  const [code, setCode] = useState('');
  const [fileName, setFileName] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  const [results, setResults] = useState(null);
  const [error, setError] = useState(null);
  const fileInputRef = useRef(null);
  const navigate = useNavigate();

  const handleFileChange = async (event) => {
    const file = event.target.files[0];
    if (file) {
      setFileName(file.name);
      const reader = new FileReader();
      reader.onload = (e) => {
        setCode(e.target.result);
      };
      reader.readAsText(file);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);
    setIsLoading(true);
    const formData = new FormData();
    formData.append('file', fileInputRef.current.files[0]);

    try {
      const response = await axios.post('http://localhost:8080/upload', formData, {
        headers: { 'Content-Type': 'multipart/form-data' },
      });

      if (response.status !== 200) {
        throw new Error('Failed to optimize code');
      }

      const { optimizedCode, explanation } = response.data;

      setResults({ optimizedCode, explanation });
      // console.log({ optimizedCode, explanation });
      navigate('/results', { state: { results: { optimizedCode, explanation } } });
    } catch (err) {
      setError(err.message);
    } finally {
      setIsLoading(false);
    }
  };

  const clearFile = () => {
    setCode('');
    setFileName('');
    if (fileInputRef.current) {
      fileInputRef.current.value = '';
    }
  };

  return (
    <>
      {isLoading ? (
        <div className="fixed inset-0 flex items-center justify-center backdrop-blur-sm bg-white z-50">
          <OptimizationResults isLoading={isLoading} results={results} />
        </div>
      ) : (
        <div className="w-full max-w-4xl mx-auto p-6">
          <form onSubmit={handleSubmit} className="space-y-6">
            {/* Upload Section */}
            <div className="space-y-4">
              <div className="flex items-center justify-between">
                <h2 className="text-xl font-semibold text-gray-800">Upload Code</h2>
                {fileName && (
                  <button
                    type="button"
                    onClick={clearFile}
                    className="text-gray-500 hover:text-gray-700"
                  >
                    <X className="w-5 h-5" />
                  </button>
                )}
              </div>

              {/* Upload Area */}
              <div className="relative">
                <input
                  type="file"
                  ref={fileInputRef}
                  onChange={handleFileChange}
                  accept=".c"
                  className="hidden"
                  id="codeFile"
                />
                <label
                  htmlFor="codeFile"
                  className={`flex flex-col items-center justify-center w-full p-6 border-2 border-dashed rounded-lg cursor-pointer 
                    ${
                      fileName
                        ? 'border-cyan-600 bg-cyan-50'
                        : 'border-gray-300 hover:border-gray-400'
                    }`}
                >
                  <Upload className={`w-8 h-8 ${fileName ? 'text-cyan-600' : 'text-gray-400'}`} />
                  <p className="mt-2 text-sm text-gray-600">
                    {fileName || 'Drop your code file here or click to browse'}
                  </p>
                  {fileName && (
                    <p className="mt-1 text-sm text-cyan-600 font-medium">{fileName}</p>
                  )}
                </label>
              </div>

              {/* Code Preview */}
              {code && (
                <div className="rounded-lg border border-gray-200 bg-gray-50">
                  <div className="flex items-center justify-between p-3 border-b border-gray-200">
                    <div className="flex items-center space-x-2">
                      <Eye className="w-4 h-4 text-gray-500" />
                      <span className="text-sm font-medium text-gray-700">Code Preview</span>
                    </div>
                  </div>
                  <div className="overflow-auto max-h-[300px] text-left">
                    <pre className="p-4 text-sm font-mono text-gray-800">{code}</pre>
                  </div>
                </div>
              )}

              {/* Submit Button */}
              <button
                type="submit"
                disabled={!code || isLoading}
                className={`w-full py-3 px-4 rounded-lg text-white font-medium transition-all
                  ${
                    code && !isLoading
                      ? 'bg-gradient-to-r from-cyan-600 to-blue-600 hover:from-cyan-700 hover:to-blue-700'
                      : 'bg-gray-300 cursor-not-allowed'
                  }`}
              >
                {isLoading ? 'Processing...' : 'Optimize Code'}
              </button>
            </div>
          </form>

          {/* Results Section */}
          {results && !isLoading && (
            <div className="mt-8 h-16">
              <OptimizationResults results={results} />
            </div>
          )}
        </div>
      )}
    </>
  );
};

export default CodeUploadForm;
