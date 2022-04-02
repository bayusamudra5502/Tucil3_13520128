import React from "react";

export default function GridItem({ value }: { value: number }) {
  return value != 16 ? (
    <div className="w-[100%] h-[100%] flex items-center justify-center">
      {value}
    </div>
  ) : (
    <div className="w-[100%] h-[100%] flex items-center justify-center bg-black"></div>
  );
}
