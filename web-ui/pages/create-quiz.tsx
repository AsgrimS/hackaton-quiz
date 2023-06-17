import { API_URL } from "@/consts/api";
import {
  Box,
  Button,
  FormControl,
  FormHelperText,
  FormLabel,
  Input,
} from "@chakra-ui/react";
import { useState } from "react";

export default function CreateQuiz() {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [openQuestionsNr, setOpenQuestionsNr] = useState(0);
  const [closedQuestionsNr, setClosedQuestionsNr] = useState(0);
  const [loading, setLoading] = useState(false);

  const handleSubmit = async () => {
    if (
      title === "" ||
      description === "" ||
      openQuestionsNr < 0 ||
      openQuestionsNr > 10 ||
      closedQuestionsNr < 0 ||
      closedQuestionsNr > 10
    )
      return;

    setLoading(true);
    try {
      const response = await fetch(`${API_URL}/my-quizzes`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: JSON.stringify({
          title,
          description,
          open_questions: openQuestionsNr,
          closed_questions: closedQuestionsNr,
        }),
      });

      const quizId = await response.json();
      setLoading(false);

      await fetch(`${API_URL}/my-quizzes/${quizId}`, {
        method: "PATCH",
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
        body: JSON.stringify({
          is_published: true,
        }),
      });

      const response2 = await fetch(`${API_URL}/quizzes/${quizId}`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });

      const quiz3 = await response2.json();

      console.log(quiz3);
    } catch (e) {
      setLoading(false);
    }
  };

  if (loading)
    return <div>Generating, this can take a while, and can break</div>;

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
        <FormHelperText>FE. Quiz JS</FormHelperText>
      </Box>
      <Box>
        <FormLabel>Quiz description</FormLabel>
        <Input
          required
          value={description}
          onChange={(e) => setDescription(e.target.value)}
          isInvalid={description === ""}
        />
        <FormHelperText>FE. Quiz JS for begginers</FormHelperText>
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
          isInvalid={openQuestionsNr < 0 || closedQuestionsNr > 10}
        />
        <FormHelperText>
          Max 10 for ChatGPT performance reasons.{" "}
        </FormHelperText>
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
          isInvalid={closedQuestionsNr < 0 || closedQuestionsNr > 10}
        />
        <FormHelperText>Max 10 for ChatGPT performance reasons.</FormHelperText>
      </Box>
      <Button type="submit" colorScheme="blue" onClick={handleSubmit}>
        Generate Quiz with ChatGPT
      </Button>
    </FormControl>
  );
}
