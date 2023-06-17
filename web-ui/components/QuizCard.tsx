import {
  Card,
  CardHeader,
  CardBody,
  Heading,
  Stack,
  Box,
  Text,
  Button,
  CardFooter,
  ButtonGroup,
  Divider,
} from "@chakra-ui/react";

interface Props {
  title: string;
  description: string;
  numberOfParticipants: number;
  userPosition?: number;
}

export const QuizCard = ({
  description,
  title,
  numberOfParticipants,
  userPosition,
}: Props) => {
  return (
    <Card mr={6} mb={6}>
      <CardHeader>
        <Heading size="md">{title}</Heading>
      </CardHeader>
      <Divider />

      <CardBody>
        <Stack spacing="4">
          <Box>
            <Heading size="xs">Description</Heading>
            <Text size="xs"> {description}</Text>
          </Box>
          <Box>
            <Heading size="xs">
              Your position / Number of partipicipants
            </Heading>
            {userPosition ? (
              <Text size="xs">
                {userPosition} / {numberOfParticipants}
              </Text>
            ) : (
              <Text size="xs">You have not played this quiz yet</Text>
            )}
          </Box>
        </Stack>
      </CardBody>
      <Divider />

      <CardFooter>
        <ButtonGroup spacing="2">
          <Button variant="solid" colorScheme="blue" size="sm">
            <Text>{!userPosition ? "Start this quiz" : "Try again"}</Text>
          </Button>
        </ButtonGroup>
      </CardFooter>
    </Card>
  );
};
