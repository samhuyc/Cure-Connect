"use client";
import React from "react";

export default function FinalPage() {
  // Example data for the trials. In a real-world app, this would be fetched from an API.
  const trials = [
    {
      title: "Phase II Randomized Trial of Carboplatin+Pemetrexed+Bevacizumab+/-",
      url: "https://clinicaltrials.gov/study/NCT03786692",
      distance: "11.1 miles",
      contact: "Joseph.Treat2@fccc.edu",
    },
    {
      title: "Nivolumab Plus Ramucirumab in Patients With Recurrent, Advanced, Metastatic NSCLC",
      url: "https://clinicaltrials.gov/study/NCT03527108",
      distance: "30.0 miles",
      contact: "Hossein.Borghaei@fccc.edu",
    },
    {
      title: "Dose Attenuated Chemotherapy in Compromised Patients With Lung Cancer",
      url: "https://clinicaltrials.gov/study/NCT05800587",
      distance: "30.0 miles",
      contact: "ryan.romasko@fccc.edu",
    },
  ];

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-primary">
      {/* Leading Information */}
      <h1 className="text-3xl font-semibold text-center mb-8">
        Here are trials you may be eligible for:
      </h1>

      {/* Cards Container */}
      <div className="space-y-6 w-full max-w-2xl">
        {trials.map((trial, index) => (
          <div
            key={index}
            className="bg-white shadow-md rounded-lg p-6 flex justify-between items-center"
          >
            {/* Left side: Title and URL */}
            <div className="flex flex-col">
              <h2 className="text-gray-600 text-xl font-bold">{trial.title}</h2>
              <a
                href={trial.url}
                target="_blank"
                rel="noopener noreferrer"
                className="text-blue-500 hover:underline"
              >
                {trial.url}
              </a>
            </div>

            {/* Right side: Distance and Contact */}
            <div className="flex flex-col text-right">
              <span className="text-gray-600">Distance: {trial.distance}</span>
              <span className="text-gray-600">Contact: {trial.contact}</span>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
