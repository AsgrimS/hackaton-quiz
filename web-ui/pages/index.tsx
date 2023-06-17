import { Quiz } from "@/common/interfaces";
import { fetcher } from "@/common/utils";
import { QuizCard } from "@/components/QuizCard";
import { API_URL } from "@/consts/api";
import { Box, Heading } from "@chakra-ui/react";
import { GetServerSideProps } from "next";
import { Inter } from "next/font/google";
import { useEffect, useState } from "react";

import useSWR from "swr";

const inter = Inter({ subsets: ["latin"] });

interface Option {
  value: number;
  label: string;
}

export const getServerSideProps: GetServerSideProps<{
  options: Option[];
}> = async () => {
  const res = await fetch(`${API_URL}/quizzes`);
  const quizes: Quiz[] = await res.json();
  const options: Option[] = quizes.map((quiz) => ({
    value: quiz.id,
    label: quiz.title,
  }));
  console.log(options);
  console.log("fgadsgsdagsad");

  return { props: { options } };
};

export default function Home({ options }: { options: Option[] }) {
  const [token, setToken] = useState("");
  const [username, setUsername] = useState("");

  useEffect(() => {
    if (!!localStorage.getItem("token")) {
      setToken(localStorage.getItem("token") || "");
      setUsername(localStorage.getItem("username") || "");
    }
  }, []);

  return (
    <Box display={{ base: "flex" }} flexDir="column" gap={8}>
      <section>
        <Heading size="md" mb="2">
          Last added quizes
        </Heading>
        <Box display="flex" alignItems="start" flexWrap="wrap">
          {!options.length && "No quizes"}
          {options.slice(0, 2).map((option) => (
            <Box flex="50%" key={option.value}>
              <QuizCard
                description="This is a quiz about the history of the world"
                title={option.label}
                numberOfParticipants={69}
              />
            </Box>
          ))}
        </Box>
      </section>
      {!!token && (
        <section>
          <Heading size="md" mb="2">
            Quizes you recently completed
          </Heading>
          <Box display="flex" alignItems="start" flexWrap="wrap">
            {!options.length && "No quizes"}
            {options.slice(0, 2).map((option) => (
              <Box flex="50%" key={option.value}>
                <QuizCard
                  description="This is a quiz about the history of the world"
                  title={option.label}
                  numberOfParticipants={69}
                />
              </Box>
            ))}
          </Box>
        </section>
      )}
    </Box>
  );
}
