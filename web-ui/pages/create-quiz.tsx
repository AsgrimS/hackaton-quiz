import { Box, Button, FormControl, FormLabel, Input } from "@chakra-ui/react";

export default function CreateQuiz() {
  return (
    <FormControl display={{ base: "flex" }} flexDirection="column" gap="5">
      <Box>
        <FormLabel>Quiz title</FormLabel>
        <Input />
      </Box>
      <Box>
        <FormLabel>Quiz description</FormLabel>
        <Input />
      </Box>
      <Button>Generate Quiz</Button>
    </FormControl>
  );
}
