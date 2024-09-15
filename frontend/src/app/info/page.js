"use client";
import { useState } from "react";
import Link from "next/link";
import LogoTop from "../components/LogoTop";

export default function Info() {
  return (
    <div className="flex flex-col items-center justify-center h-screen bg-primary">
      <LogoTop />
      <div className="text-center mb-4">
        <h2 className="text-2xl font-semibold">
          Enter more details to enhance search
        </h2>
      </div>

      <div className="flex flex-col space-y-4 max-w-md w-full">
        <input
          type="text"
          placeholder="Enter your age"
          className="input input-bordered"
        />
        <input
          type="text"
          placeholder="Enter your sex"
          className="input input-bordered"
        />
        <input
          type="text"
          placeholder="Enter your location"
          className="input input-bordered"
        />
        <input
          type="text"
          placeholder="Maximum distance to travel"
          className="input input-bordered"
        />

        <div className="flex justify-between w-full max-w-md mt-8">
          <Link href="/">
            <button className="btn btn-outline">Back</button>
          </Link>
          <Link href="/question1">
            <button className="btn btn-outline">Next</button>
          </Link>
        </div>
      </div>
    </div>
  );
}
