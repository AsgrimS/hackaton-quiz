import { Leaderboard } from "@/components/Leaderboard";
import { useState } from "react";
import Select from "react-select";

interface Option {
  value: string;
  label: string;
}

const options: Option[] = [
  { value: "chocolate", label: "Chocolate" },
  { value: "strawberry", label: "Strawberry" },
  { value: "vanilla", label: "Vanilla" },
];

export default function Leaderboards() {
  const [selectedOption, setSelectedOption] = useState<Option | null>(null);
  return (
    <div>
      <Select
        options={options}
        value={selectedOption}
        onChange={setSelectedOption}
      />
      <Leaderboard />
    </div>
  );
}
