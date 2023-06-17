import { QuizCard } from "@/components/QuizCard";
import { Box, Heading } from "@chakra-ui/react";
import { Inter } from "next/font/google";

const inter = Inter({ subsets: ["latin"] });

export default function Home() {
  return (
    <Box display={{ base: "flex" }} flexDir="column" gap={8}>
      <section>
        <Heading size="md" mb="2">
          Last added quizes
        </Heading>
        <Box display="flex" alignItems="start" flexWrap="wrap">
          <Box flex="50%">
            <QuizCard
              description="This is a quiz about the history of the world"
              title="Math"
              numberOfParticipants={69}
              userPosition={1}
            />
          </Box>
          <Box flex="50%">
            <QuizCard
              description="This is a quiz about the history of the world"
              title="History"
              numberOfParticipants={199}
            />
          </Box>
        </Box>
      </section>
      <section>
        <Heading size="md" mb="2">
          Quizes you recently completed
        </Heading>
        <Box display="flex" alignItems="start" flexWrap="wrap">
          <Box flex="50%">
            <QuizCard
              description="This is a quiz about the history of the world"
              title="JS"
              numberOfParticipants={69}
              userPosition={1}
            />
          </Box>
          <Box flex="50%">
            <QuizCard
              description="This is a quiz about the history of the world"
              title="History"
              numberOfParticipants={199}
              userPosition={12}
            />
          </Box>
        </Box>
      </section>
    </Box>
  );
}
