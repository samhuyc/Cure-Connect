"use client";
import { useState } from "react";
import Image from "next/image";
import Link from "next/link";

import Logo from "../../public/Logo.png";

export default function Page() {
  const [condition, setCondition] = useState("");

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-primary">
      <Image src={Logo} alt="Logo" width={800} className="mb-8" />
      <h1 className="text-2xl font-bold mb-4">
        Take our quick quiz to get matched to open clinical tirals
      </h1>
      <div className="flex items-center space-x-4 w-full max-w-md">
        <input
          type="text"
          placeholder="Enter your conditions"
          className="input input-bordered w-full"
          value={condition}
          onChange={(e) => setCondition(e.target.value)}
        />
        <button className="btn btn-outline">
          <Link href="/info">Next</Link>
        </button>
      </div>
    </div>
  );
}
