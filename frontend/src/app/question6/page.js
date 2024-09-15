"use client";
import { useState } from "react";
import Link from "next/link";
import LogoTop from "../components/LogoTop";

export default function Questions() {
  const questionData = {
    question: "What is your QTcF value in msec?",
    question_type: true,
  };

  const [selectedButton, setSelectedButton] = useState(null);
  const [inputValue, setInputValue] = useState("");

  const handleButtonClick = (buttonValue) => {
    setSelectedButton(buttonValue);
    if (buttonValue === "I don't know") {
      setInputValue("");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-primary">
      <LogoTop />

      <h1 className="text-2xl font-bold mb-4">{questionData.question}</h1>

      {questionData.question_type === false ? (
        <div className="flex flex-col space-y-4 w-full max-w-md">
          <button
            className={`btn w-full btn-outline ${
              selectedButton === "True"
                ? "bg-secondary text-white border-0 outline-none"
                : "bg-white"
            }`}
            onClick={() => handleButtonClick("True")}
          >
            Yes
          </button>
          <button
            className={`btn w-full btn-outline ${
              selectedButton === "False"
                ? "bg-secondary text-white border-0 outline-none"
                : "bg-white"
            }`}
            onClick={() => handleButtonClick("False")}
          >
            No
          </button>
          <button
            className={`btn w-full btn-outline ${
              selectedButton === "I don't know"
                ? "bg-secondary text-white border-0 outline-none"
                : "bg-white"
            }`}
            onClick={() => handleButtonClick("I don't know")}
          >
            I don't know
          </button>
        </div>
      ) : (
        <div className="flex flex-col space-y-4 w-full max-w-md">
          <input
            type="text"
            placeholder="Enter numerical value"
            className="input input-bordered w-full"
            value={inputValue}
            onChange={(e) => {
              setInputValue(e.target.value);
              setSelectedButton(null);
            }}
          />
          <button
            className={`btn w-full btn-outline ${
              selectedButton === "I don't know"
                ? "bg-secondary text-white border-0 outline-none"
                : "bg-white"
            }`}
            onClick={() => handleButtonClick("I don't know")}
          >
            I don't know
          </button>
        </div>
      )}

      <div className="flex justify-between w-full max-w-md mt-8">
        <Link href="/question5">
          <button className="btn btn-outline">Back</button>
        </Link>
        <Link href="/question7">
          <button className="btn btn-outline">Next</button>
        </Link>
      </div>
    </div>
  );
}
