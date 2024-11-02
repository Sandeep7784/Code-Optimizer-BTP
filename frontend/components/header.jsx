import React from "react";
import { UserCircle } from "lucide-react";
import icon_img from "../images/favicon.png";
import man from "../images/man.png";

const Header = ({ userName = "Sandeep" }) => {
  return (
    <header className="bg-white border-b border-gray-100">
      <div className="container mx-auto px-6">
        <div className="flex h-16 justify-between items-center">
          {/* Logo and Title */}
          <div className="flex items-center gap-3">
            <div
              className="flex items-center gap-2 hover:opacity-80 transition-opacity cursor-pointer"
              onClick={() => (window.location.href = "/")}
            >
              <img
                src={icon_img}
                alt="Icon"
                className="w-9 h-9 rounded-lg shadow-sm"
              />
              <h1 className="text-xl font-bold bg-gradient-to-r from-cyan-600 to-blue-600 bg-clip-text text-transparent">
                Code Optimizer
              </h1>
            </div>
          </div>
          {/* User Section */}
          <div className="flex items-center gap-4">
            <div className="hidden sm:flex items-center gap-3 px-4 py-2 rounded-lg bg-gray-50 hover:bg-gray-100 transition-colors duration-200">
              <p className="text-sm font-medium text-gray-700">
                Hello, {userName}
              </p>
              <img src={man} alt="User" className="w-6 h-6 rounded-full" />
            </div>

            {/* Mobile User Icon */}
            <div className="sm:hidden">
              <img src={man} alt="User" className="w-7 h-7 rounded-full" />
            </div>
          </div>
        </div>
      </div>
    </header>
  );
};

export default Header;
