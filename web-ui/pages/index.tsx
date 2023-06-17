import { QuizCard } from "@/components/QuizCard";
import { Box, Heading } from "@chakra-ui/react";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <section>
      <Heading size="md" mb="2">
        Last added quizes
      </Heading>
      <Box display="flex" alignItems="start" flexWrap="wrap">
        <Box flex="50%">
          <QuizCard
            description="This is a quiz about the history of the world"
            title="History"
          />
        </Box>
        <Box flex="50%">
          <QuizCard
            description="This is a quiz about the history of the world"
            title="History"
          />
        </Box>
        <Box flex="50%">
          <QuizCard
            description="This is a quiz about the history of the world"
            title="History"
          />
        </Box>
      </Box>
    </section>
  );
}
