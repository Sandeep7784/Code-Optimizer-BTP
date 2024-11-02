import React from 'react';
import CodeUploadForm from 'CodeUploadForm';

const CodeOptimizationTool = () => {
  return (
    <div className="flex flex-col min-h-screen">
      <div className="container mx-auto flex-grow flex items-center">
        <div className="w-full">
          <div className="text-center mb-8">
            <h1 className="text-3xl font-bold mb-2">Code Optimizer</h1>
            <p className="text-xl">Upload your C/C++ code for optimization</p>
          </div>
          <CodeUploadForm />
        </div>
      </div>
    </div>
  );
};

export default CodeOptimizationTool;