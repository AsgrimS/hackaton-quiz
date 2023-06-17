import { Quiz } from "@/common/interfaces";
import { Leaderboard } from "@/components/Leaderboard";
import { GetServerSideProps } from "next";
import { useState } from "react";
import Select from "react-select";

interface Option {
  value: number;
  label: string;
}

export const getServerSideProps: GetServerSideProps<{
  options: Option[];
}> = async () => {
  const res = await fetch("http://localhost:8000/api/quizzes");
  const quizes: Quiz[] = await res.json();
  const options: Option[] = quizes.map((quiz) => ({
    value: quiz.id,
    label: quiz.title,
  }));
  return { props: { options } };
};

export default function Leaderboards({ options }: { options: Option[] }) {
  const [selectedOption, setSelectedOption] = useState<Option | null>(null);

  return (
    <div>
      <Select
        options={options}
        value={selectedOption}
        onChange={setSelectedOption}
        placeholder="Start typing to search for a quiz..."
      />
      {selectedOption && <Leaderboard quizId={selectedOption.value} />}
    </div>
  );
}
