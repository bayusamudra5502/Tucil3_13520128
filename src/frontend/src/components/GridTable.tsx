import React from "react";
import GridItem from "./GridItem";

export default function GridTable({ grid }: { grid: number[] }) {
  return (
    <div className="grid grid-cols-4 gap-2">
      {grid.map((value) => (
        <GridItem value={value}></GridItem>
      ))}
    </div>
  );
}
