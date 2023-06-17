import { Box, Button, FormControl, FormLabel, Input } from "@chakra-ui/react";
import { useState } from "react";

export default function CreateQuiz() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [openQuestionsNr, setOpenQuestionsNr] = useState(0);
  const [closedQuestionsNr, setClosedQuestionsNr] = useState(0);

  const handleSubmit = () => {
    console.log(title, description, openQuestionsNr, closedQuestionsNr);
  };

  return (
    <FormControl display={{ base: "flex" }} flexDirection="column" gap="5">
      <Box>
        <FormLabel>Quiz title</FormLabel>
        <Input
          required
          value={title}
          onChange={(e) => setTitle(e.target.value)}
          isInvalid={title === ""}
        />
      </Box>
      <Box>
        <FormLabel>Quiz description</FormLabel>
        <Input
          required
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          isInvalid={description === ""}
        />
      </Box>
      <Box>
        <FormLabel>Number of open questions</FormLabel>
        <Input
          required
          value={openQuestionsNr}
          onChange={(e) => {
            if (!isNaN(Number(e.target.value)))
              setOpenQuestionsNr(Number(e.target.value));
          }}
          isInvalid={openQuestionsNr < 0}
        />
      </Box>

      <Box>
        <FormLabel>Number of closed questions</FormLabel>
        <Input
          required
          value={closedQuestionsNr}
          onChange={(e) => {
            if (!isNaN(Number(e.target.value)))
              setClosedQuestionsNr(Number(e.target.value));
          }}
          isInvalid={closedQuestionsNr < 0}
        />
      </Box>
      <Button type="submit" colorScheme="blue" onClick={handleSubmit}>
        Generate Quiz with ChatGPT
      </Button>
    </FormControl>
  );
}
